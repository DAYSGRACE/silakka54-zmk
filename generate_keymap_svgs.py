#!/usr/bin/env python3
"""
Genera SVGs de todas las capas del keymap silakka54 a partir de config/silakka54.keymap
y usando el layout físico de config/silakka54.json
"""

import re
import os
import json
import math

# Config
KEYMAP_FILE = "config/silakka54.keymap"
LAYOUT_FILE = "config/silakka54.json"
OUTPUT_DIR = "assets"
SCALE = 60  # Pixels per key unit
KEY_SIZE = 50 # Size of key square
PADDING = 5

# Mapeo de nombres para que sean legibles
KEY_LABELS = {
    "NUMBER_1": "1", "NUMBER_2": "2", "NUMBER_3": "3", "NUMBER_4": "4", "NUMBER_5": "5",
    "NUMBER_6": "6", "NUMBER_7": "7", "NUMBER_8": "8", "NUMBER_9": "9", "NUMBER_0": "0",
    "N1": "1", "N2": "2", "N3": "3", "N4": "4", "N5": "5",
    "N6": "6", "N7": "7", "N8": "8", "N9": "9", "N0": "0",
    "LEFT_COMMAND": "GUI", "LCMD": "GUI", "RCMD": "GUI",
    "LEFT_CONTROL": "CTRL", "LCTRL": "CTRL", "RCTRL": "CTRL",
    "LEFT_SHIFT": "SHFT", "LSHFT": "SHFT", "RSHFT": "SHFT",
    "LEFT_ALT": "ALT", "LALT": "ALT", "RALT": "ALT",
    "BACKSPACE": "BSPC", "DELETE": "DEL", "ENTER": "ENT", "SPACE": "SPC",
    "TAB": "TAB", "ESCAPE": "ESC",
    "C_VOLUME_UP": "VOL+", "C_VOL_UP": "VOL+", "C_VOLUME_DOWN": "VOL-", "C_VOL_DN": "VOL-",
    "C_MUTE": "MUTE", "C_PLAY_PAUSE": "PLAY", "C_NEXT": "NEXT", "C_PREV": "PREV",
    "C_BRIGHTNESS_INC": "BRI+", "C_BRIGHTNESS_DEC": "BRI-",
    "PAGE_UP": "PgUp", "PAGE_DOWN": "PgDn", "HOME": "HOME", "END": "END",
    "UP_ARROW": "↑", "DOWN_ARROW": "↓", "LEFT_ARROW": "←", "RIGHT_ARROW": "→",
    "LEFT": "←", "RIGHT": "→", "UP": "↑", "DOWN": "↓",
    "EXCLAMATION": "!", "AT_SIGN": "@", "HASH": "#", "DOLLAR": "$", "PERCENT": "%",
    "CARET": "^", "AMPERSAND": "&", "ASTERISK": "*", "LPAR": "(", "RPAR": ")",
    "MINUS": "-", "EQUAL": "=", "PLUS": "+", "UNDERSCORE": "_",
    "LBRC": "[", "RBRC": "]", "LBKT": "[", "RBKT": "]",
    "PIPE": "|", "BACKSLASH": "\\", "SLASH": "/", "QUESTION": "?",
    "SEMICOLON": ";", "COLON": ":", "SQT": "'", "DQT": '"', "SINGLE_QUOTE": "'",
    "COMMA": ",", "PERIOD": ".", "DOT": ".", "GRAVE": "`", "TILDE": "~",
    "CAPSLOCK": "CAPS", "PRINTSCREEN": "PRT", "SCROLLLOCK": "SCR", "PAUSE": "PAUSE",
    "INSERT": "INS", 
    "BT_CLR_ALL": "BT CLR", "BT_NXT": "BT >", "BT_PRV": "BT <",
    "TRANS": "", "TRNS": ""
}

def load_layout():
    with open(LAYOUT_FILE, 'r') as f:
        data = json.load(f)
    # Extract list of key positions
    # Assuming the first layout in layout dict is the one we want
    layout_name = list(data['layouts'].keys())[0]
    return data['layouts'][layout_name]['layout']

def parse_keymap():
    with open(KEYMAP_FILE, 'r') as f:
        content = f.read()

    layers = {}
    layer_pattern = r'(\w+)\s*\{[\s\n]*bindings\s*=\s*<(.*?)>;'
    
    for match in re.finditer(layer_pattern, content, re.DOTALL):
        layer_name = match.group(1)
        bindings_str = match.group(2)
        # Check if bindings are cleaner
        bindings_str = re.sub(r'/\*.*?\*/', '', bindings_str, flags=re.DOTALL) # remove comments
        
        # Split tokens
        tokens = []
        current_token = ""
        depth = 0
        
        # Simple parser to handle spaces and &kp etc
        clean_str = bindings_str.replace('\n', ' ').strip()
        parts = [p for p in clean_str.split(' ') if p.strip()]
        
        keys = []
        for p in parts:
            if p.startswith('&'):
                keys.append(p.replace('&', ''))
            elif p.startswith('(') or p.endswith(')'):
                # Handle macros or special params roughly
                pass 
                
        # Better extraction: just grab words starting with & or plain words if valid
        # This regex grabs keys like &kp A, &mo 1, etc.
        keys = [x.strip() for x in re.findall(r'&[a-zA-Z0-9_]+(?:\s+[a-zA-Z0-9_]+)?', bindings_str)]
        
        # Clean up the keys list
        cleaned_keys = []
        for k in keys:
            # remove &
            k = k[1:]
            cleaned_keys.append(k)
            
        layers[layer_name] = cleaned_keys
        
    return layers

def clean_label(key_raw):
    # key_raw like "kp A", "mo 1", "msc SCRL_UP"
    parts = key_raw.split()
    if not parts: return ""
    
    behavior = parts[0]
    param = parts[1] if len(parts) > 1 else ""
    
    label = ""
    
    if behavior == "kp":
        label = KEY_LABELS.get(param, param)
    elif behavior == "mo":
        label = f"L{param}"
    elif behavior == "mt":
        # Mod-Tap: &mt LSHIFT A -> "Sft/A"
        mod = parts[1] if len(parts) > 1 else ""
        tap = parts[2] if len(parts) > 2 else ""
        label = f"{KEY_LABELS.get(mod, mod)}/{KEY_LABELS.get(tap, tap)}"
    elif behavior == "bt":
        label = KEY_LABELS.get(f"BT_{param}", f"BT {param}")
    elif behavior == "trans":
        label = "↓"
    elif behavior == "none":
        label = ""
    else:
        # Fallback
        full = "_".join(parts[1:]) if len(parts) > 1 else behavior
        label = KEY_LABELS.get(full, full)
        if label == full and len(label) > 6:
             label = label[:6]
             
    return label.upper()

def generate_svg(layer_name, keys, layout_data):
    # Calculate bounds
    max_x = max(item['x'] for item in layout_data) + 1
    max_y = max(item['y'] for item in layout_data) + 1
    
    width = int(max_x * SCALE) + 20
    height = int(max_y * SCALE) + 50
    
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">')
    svg.append(f'<style>')
    svg.append('.key { fill: #f0f0f0; stroke: #666; stroke-width: 1; rx: 4; }')
    svg.append('.label { font-family: sans-serif; font-size: 12px; text-anchor: middle; fill: #333; }')
    svg.append('.sub { font-size: 9px; fill: #888; }')
    svg.append('.mod { fill: #e0e0e0; }')
    svg.append('.layer { fill: #d1c4e9; }')
    svg.append('.special { fill: #b3e5fc; }')
    svg.append('</style>')
    
    svg.append(f'<text x="20" y="30" font-family="sans-serif" font-size="20" font-weight="bold">Layer: {layer_name}</text>')
    
    # Check count
    if len(keys) != len(layout_data):
        print(f"Warning: Layer {layer_name} has {len(keys)} keys, layout has {len(layout_data)} positions. Truncating/Filling.")
    
    for i, item in enumerate(layout_data):
        if i >= len(keys): break
        
        k = keys[i]
        label = clean_label(k)
        
        # Position
        x = item['x'] * SCALE + 10
        y = item['y'] * SCALE + 40
        w = KEY_SIZE
        h = KEY_SIZE
        
        # Rotation? - Ignoring for now for readability, or simplest approximation
        # If rotation exists, SVG rotate
        r = item.get('r', 0)
        transform = ""
        if r != 0:
            # Pivot around center of key? usually r is around a specific point, often x,y
            # Simplified: just draw rect. The user wants to see "what is where".
            # Perfect reconstruction requires parsing 'rx', 'ry' from JSON which are rotation origins.
            pass
            
        # Color coding
        cls = "key"
        if k.startswith("mo "): cls += " layer"
        elif k.startswith("kp L") or k.startswith("kp R"): cls += " mod" # heuristic for mods
        elif label in ["ENT", "ESC", "BSPC", "TAB"]: cls += " special"
        
        svg.append(f'<g transform="translate({x},{y})">')
        svg.append(f'<rect class="{cls}" width="{w}" height="{h}" />')
        
        # Center text
        # If label is long, split lines?
        svg.append(f'<text x="{w/2}" y="{h/2 + 5}" class="label">{label}</text>')
        svg.append('</g>')
        
    svg.append('</svg>')
    return '\n'.join(svg)

def main():
    layout = load_layout()
    layers = parse_keymap()
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    for name, keys in layers.items():
        print(f"Generating {name}...")
        svg = generate_svg(name, keys, layout)
        with open(f"{OUTPUT_DIR}/silakka54_keymap_{name}.svg", "w") as f:
            f.write(svg)
            
    print("Done.")

if __name__ == "__main__":
    main()

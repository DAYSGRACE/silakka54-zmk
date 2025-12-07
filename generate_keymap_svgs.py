#!/usr/bin/env python3
"""
Genera SVGs de todas las capas del keymap silakka54 a partir de config/silakka54.keymap
"""

import re
import os

# Parsear el keymap
keymap_file = "config/silakka54.keymap"
with open(keymap_file, 'r') as f:
    content = f.read()

# Extraer cada capa
layers = {}
layer_pattern = r'(\w+)\s*\{[\s\n]*bindings\s*=\s*<(.*?)>;'
for match in re.finditer(layer_pattern, content, re.DOTALL):
    layer_name = match.group(1)
    bindings_str = match.group(2)
    # Limpiar bindings
    bindings_str = bindings_str.replace('\n', ' ').replace('&', '').strip()
    # Dividir por espacios, filtrar vacíos
    keys = [k.strip() for k in bindings_str.split() if k.strip()]
    layers[layer_name] = keys

print(f"Found {len(layers)} layers: {list(layers.keys())}")

# Funciones para generar SVG
def truncate_key(key_text, max_len=8):
    """Truncate key text to fit in the key box"""
    if len(key_text) > max_len:
        return key_text[:max_len-1] + "."
    return key_text

def color_for_key(key_text):
    """Return color based on key type"""
    key_lower = key_text.lower()
    if key_lower.startswith("mo"):
        return "#ffe0b2"  # orange for layer keys
    elif key_lower in ["space", "bksp", "enter", "backspace", "tab"]:
        return "#c8e6c9"  # green for common modifiers
    elif key_lower.startswith("kp"):
        return "#f7f7f7"  # light for regular keys
    else:
        return "#bbdefb"  # blue for special
    
def generate_svg(layer_name, keys):
    """Generate SVG for a layer"""
    # Layout: 4 rows of 12 keys + 6 thumbs
    rows = [
        keys[0:12],   # row 1
        keys[12:24],  # row 2
        keys[24:36],  # row 3
        keys[36:48],  # row 4
    ]
    thumbs = keys[48:54] if len(keys) > 48 else []
    
    svg_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<svg xmlns="http://www.w3.org/2000/svg" width="1500" height="700" viewBox="0 0 1500 700">',
        '  <style>',
        '    .k{fill:#f7f7f7;stroke:#333;stroke-width:2}',
        '    .kl{font:14px monospace;fill:#111;text-anchor:middle}',
        '    .title{font:20px sans-serif;fill:#111;font-weight:bold}',
        '  </style>',
        f'  <text x="750" y="30" class="title">Silakka54 - Layer: {layer_name}</text>',
        '  <g transform="translate(60,60)">',
    ]
    
    # Draw keys for each row
    for row_idx, row in enumerate(rows):
        y_offset = row_idx * 110
        for col_idx, key_text in enumerate(row):
            x_offset = col_idx * 110
            key_label = key_text.replace("kp ", "").replace("mo ", "").upper()
            color = color_for_key(key_text)
            
            svg_lines.append(f'    <!-- R{row_idx+1}C{col_idx+1} -->')
            svg_lines.append(f'    <g transform="translate({x_offset},{y_offset})">')
            svg_lines.append(f'      <rect class="k" x="0" y="0" width="90" height="70" rx="6" ry="6" fill="{color}"/>')
            svg_lines.append(f'      <text x="45" y="40" class="kl">{truncate_key(key_label, 7)}</text>')
            svg_lines.append(f'    </g>')
    
    # Draw thumb cluster
    if thumbs:
        svg_lines.append('    <!-- Thumb cluster -->')
        thumb_y = len(rows) * 110 + 30
        thumb_labels = [t.replace("kp ", "").replace("mo ", "").upper() for t in thumbs]
        thumb_positions = [0, 110, 220, 430, 540, 650]  # spacing
        
        for idx, (label, x_pos) in enumerate(zip(thumb_labels, thumb_positions)):
            color = color_for_key(thumbs[idx])
            width = 190 if idx == 2 else 90  # space bar is wider
            svg_lines.append(f'    <!-- T{idx+1} -->')
            svg_lines.append(f'    <g transform="translate({x_pos},{thumb_y})">')
            svg_lines.append(f'      <rect class="k" x="0" y="0" width="{width}" height="70" rx="6" ry="6" fill="{color}"/>')
            svg_lines.append(f'      <text x="{width//2}" y="40" class="kl">{truncate_key(label, 7)}</text>')
            svg_lines.append(f'    </g>')
    
    svg_lines.extend([
        '  </g>',
        '</svg>'
    ])
    
    return '\n'.join(svg_lines)

# Generate SVGs for each layer
os.makedirs('assets', exist_ok=True)
for layer_name, keys in layers.items():
    svg_content = generate_svg(layer_name, keys)
    filename = f'assets/silakka54_keymap_{layer_name}.svg'
    with open(filename, 'w') as f:
        f.write(svg_content)
    print(f"Generated {filename}")

print("All SVGs generated successfully!")

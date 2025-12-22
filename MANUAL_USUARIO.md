# Manual de Usuario - Teclado Silakka54

Este documento describe el funcionamiento, atajos y capas configuradas en tu teclado Silakka54.

## 🗺️ Visión General
El Silakka54 es un teclado de 6 columnas y (principalmente) 4 filas + teclas de pulgar.
Debido a su tamaño compacto, muchas teclas se acceden mediante **Capas (Layers)** o **Combinaciones (Combos)**.

### ⌨️ Capa Base (Default Layer)
Es la capa que usas para escribir normalmente.
- **Letras y Números**: Disposición estándar QWERTY.
- **Teclas de Sistema**:
  - `ESC`: Esquina superior izquierda.
  - `LCTRL`: Esquina inferior izquierda.
  - `BSPC` (Borrar): Tercera tecla del pulgar (Mano Izquierda, interior).
  - `SPACE` (Espacio): Cuarta tecla del pulgar (Mano Derecha, interior).

## ↩️ Cómo hacer ENTER
El teclado **NO** tiene una tecla dedicada para Enter en la capa base.
Para enviar un Enter, usa el siguiente **Combo**:
- Presiona **J + K + L** al mismo tiempo.
- (Son las teclas centrales de la mano derecha en la fila de descanso).

---

## 🎛️ Teclas de Pulgar (Thumb Keys) y Capas
Las teclas de los pulgares son fundamentales para "activar" otras funciones mientras las mantienes presionadas.
Orden de izquierda a derecha (3 en mano izq, 3 en mano der):

1. **`mo 2`** (Capa 2): Símbolos/Nav.
2. **`mo 1`** (Capa 1): Media/Mouse.
3. **`BSPC`** (Borrar).
4. **`SPACE`** (Espacio).
5. **`mo 3`** (Capa 3): Teclas F.
6. **`mo 5`** (Capa 5): Teclado Numérico.

---

## 📑 Detalle de Capas

### Capa 1 (Mantener `mo 1` / Pulgar Izquierdo Centro)
Enfocada en multimedia, navegación y control del mouse.
- **Inicio de Windows (GUI)**: Esquina inferior izquierda (donde está Control normalmente).
- **Mouse**:
  - Movimiento: `E`, `S`, `D`, `F` (Arriba, Izq, Abajo, Der).
  - Clics: Teclas de pulgar de la mano derecha (Izq, Der, Medio).
  - Scroll: `W` (Bajar), `R` (Subir). (Nota: Verifica si es R/W o teclas adyacentes según tu comodidad, en config es `msc SCRL_DOWN` en W y `msc SCRL_UP` en R).
- **Multimedia**:
  - Volumen: `_` (Vol-) y `+` (Vol+) en la fila superior derecha (posiciones 10 y 11).
  - Reproducción: `I` (Play/Pause), `U` (Prev), `O` (Next).
- **Navegación**:
  - Flechas: `K` (Abajo), `I` (Arriba), `J` (Izq), `L` (Der). (Nota: Revisa visualmente ya que UP suele estar en I o U).
    - En tu config: `UP` en I, `DOWN` en K, `LEFT` en J, `RIGHT` en L. (Estilo VI).
  - `Home`/`End`, `PageUp`/`PageDown` en la mano derecha.

### Capa 2 (Mantener `mo 2` / Pulgar Izquierdo Exterior)
Enfocada en símbolos y movimientos rápidos.
- **Inicio de Windows (GUI)**: Pulgar Derecho Interior (donde suele estar Espacio).
- **Flechas**: Mano Izquierda (`S` Izq, `D` Abajo, `F` Der, `E` Arriba).
- **Símbolos**: 
  - Corchetes `[` y `]` en `P` y `[` originales.
  - Menos `-` y Igual `=` en fila superior derecha.
- **Modificadores**: `BloqMayús` (Caps Lock) en pulgar izquierdo centro.

### Capa 3 (Mantener `mo 3` / Pulgar Derecho Centro)
- **Teclas F**: `F1` a `F12` en la fila superior de números.
- **Bluetooth**: 
  - `BT_CLR` (Borrar conexión): **Esquina inferior derecha** (Tecla MO4). Úsalo para desvincular.
  - `BT_PRV` / `BT_NXT`: Teclas `.` y `/` (Period y Slash). Cambio de Perfiles.

### Capa 5 (Mantener `mo 5` / Pulgar Derecho Exterior)
- **Numpad**: Convierte la mano derecha en un teclado numérico.
  - `7`, `8`, `9` en `U`, `I`, `O`.
  - `4`, `5`, `6` en `J`, `K`, `L`.
  - `1`, `2`, `3` en `M`, `,`, `.`.
  - `0` en la tecla **`>`** (abajo del `2` / tecla SLASH original).

---

## 🔡 Acentos y Caracteres Especiales

### Acentos (á, é, í, ó, ú) y Ñ
Depende de tu configuración de **Idioma en Windows**:
1.  **Si usas "Estados Unidos - Internacional"**:
    - **Acentos**: Presiona `'` (comilla simple) y luego la vocal. (Ej: `'` + `a` = `á`).
    - **Ñ**: Presiona `~` (Shift + Grave) y luego `n`. (Ej: `~` + `n` = `ñ`) o usa `ALT Derecha` + `n`.
2.  **Si usas "Español"**:
    - Las teclas coincidirán con la posición física del teclado español estándar.
    - La tilde `´` suele estar al lado de la `ñ` (o `P` en este layout).
    - La `ñ` suele estar en `;`.

### Dónde están los símbolos faltantes
En la **Capa 2** (`mo 2`):
- **`+` (Más)** y **`=` (Igual)**: Esquina superior derecha.
- **`` ` `` (Backtick) y `~` (Tilde)**:
  - **Backtick (`` ` ``)**: Esquina superior izquierda (donde iría Tab/Esc), tecla `GRAVE`.
  - **Tilde (`~`)**: Presiona `Shift` + esa misma tecla `GRAVE`.
- **Mayúsculas (Caps Lock)**:
  - Pulgar Izquierdo Centro (al lado de `mo 2`) en la Capa 2.

### Bluetooth (Capa 3)
- **Cambio de Perfil**: Teclas `.` y `/`.
- **Reset conex**: Tecla esquina inferior derecha (`MO 4`).

## 🎨 Imágenes de Referencia
Puedes consultar los diagramas generados en la carpeta `assets` para ver visualmente cada capa:
- `silakka54_keymap_default_layer.svg`
- `silakka54_keymap_L1.svg`
- Etc.

## 🛠️ Solución de Problemas

### Problemas de Bluetooth
Si tienes problemas para que tu PC detecte el teclado:
1. **Reiniciar Conexiones**:
   - En **Capa 3**, presiona la tecla de la **esquina inferior derecha**.
   - Esto borrará la conexión del perfil actual. Windows pedirá emparejar de nuevo.
2. **Cambiar Perfil**:
   - En **Capa 3**, usa `.` (anterior) y `/` (siguiente).

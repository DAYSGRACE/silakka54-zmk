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

### Capa 5 (Mantener `mo 5` / Pulgar Derecho Exterior)
- **Numpad**: Convierte la mano derecha en un teclado numérico.
  - `7`, `8`, `9` en `U`, `I`, `O`.
  - `4`, `5`, `6` en `J`, `K`, `L`.
  - `1`, `2`, `3` en `M`, `,`, `.`.

---

## 🎨 Imágenes de Referencia
Puedes consultar los diagramas generados en la carpeta `assets` para ver visualmente cada capa:
- `silakka54_keymap_default_layer.svg`
- `silakka54_keymap_L1.svg`
- Etc.

## 🛠️ Solución de Problemas

### Problemas de Bluetooth
Si tienes problemas para que tu PC detecte el teclado:
1. **Reiniciar Conexiones (BT Clear)**:
   - Ve a la **Capa 1** (manteniendo `mo 1`, pulgar izquierdo centro).
   - Presiona la tecla **`\`** (esquina inferior derecha, donde suele estar `BT_CLR_ALL` en el keymap).
   - Esto borrará todos los perfiles guardados en el teclado.
   - *Nota: Asegúrate de también "Olvidar dispositivo" en Windows.*
2. **Cambiar Perfil**:
   - En **Capa 1**, usa las teclas de la columna derecha para cambiar entre perfiles (si están configurados).

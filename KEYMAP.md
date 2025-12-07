**Silakka54 — Keymap reference**

Este archivo documenta el `keymap` que actualmente se usa para compilar el firmware.

Ubicación del keymap usado en compilación:
- `config/silakka54.keymap`

Resumen: cada "layer" está listado abajo; las abreviaturas comunes:
- `&kp KEY`: keypress (ej. `&kp A` = tecla A)
- `&mo N`: momentary layer N (mantener para acceder a la capa N)
- `&trans`: transparente (hereda de la capa inferior)
- `mkp` / `mmv` / `msc` / `bt`: comportamientos especiales (mouse, multimedia, bluetooth)

---

DEFAULT (capa principal)
Fila 1: ESC, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, DELETE
Fila 2: TAB, Q, W, E, R, T, Y, U, I, O, P, BACKSLASH
Fila 3: LSHIFT, A, S, D, F, G, H, J, K, L, SEMICOLON, SINGLE_QUOTE
Fila 4: LCTRL, Z, X, C, V, B, N, M, COMMA, PERIOD, SLASH, MO 4
Thumbs / centro: MO 2, MO 1, SPACE, BACKSPACE, MO 3, MO 5

Notas: `MO 1..5` son capas momentáneas que se activan mientras mantienes la tecla.

---

L1 (capa 1 — funciones/media)
- Llaves multimedia y navegación (brightness, media, bt clear/pairing, flechas, home/end, page up/down, undo/cut/copy/paste, etc.)

L2 (capa 2)
- Teclas de símbolos, flechas y CAPSLOCK en thumb cluster

L3 (capa 3)
- F1..F12 arriba; modificadores alternos (ej. ESC, ALT, CMD combos)

L4 (capa 4)
- Principalmente transparentes, con `MO 4` en corner

L5 (capa 5)
- Layout numpad en la parte derecha (números N1..N9)

---

Cómo editar el layout y volver a compilar:
1. Edita `config/silakka54.keymap` y cambia las entradas `&kp ...` por la tecla deseada.
2. Guarda, haz commit y push al repo:

```powershell
cd "a:/keyboard configuration/zmk-config-silakka54"
git add config/silakka54.keymap
git commit -m "Update keymap: nombre del cambio"
git push
```

3. GitHub Actions se disparará automáticamente y generará nuevos artefactos (.uf2) para left/right.

4. Descarga los artefactos desde Actions → el run correspondiente → Artifacts → `firmware`.

5. Flashea: primero `settings_reset` (si lo deseas), luego `silakka54_left-*.uf2` y `silakka54_right-*.uf2`.

Cómo ver/editar el keymap en una UI (ZMK configurator / Studio):
- Algunas interfaces web (ZMK Studio / nice!studio) esperan que el repo tenga los metadatos `boards/shields/<shield>/*.zmk.yml` y un `build.yaml` — tu repo ya tiene `silakka54.zmk.yml` y `build.yaml`.
- En la UI de ZMK que uses, añade tu repo (URL GitHub) como config repo o selecciona "Import from GitHub". Si la UI no muestra el shield, intenta usar la opción "custom repo" con la URL de este repo y selecciona el shield `silakka54_left` / `silakka54_right`.

Si quieres, puedo:
- Generar una imagen SVG/PNG con etiquetas de cada tecla (visual) a partir del `keymap` actual.
- Añadir un archivo `keymap_notes.md` con una tabla por tecla (pos -> acción) para facilitar la edición.

Dime cuál prefieres y lo agrego al repo.

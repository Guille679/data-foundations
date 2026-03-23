# Guía 5: Entrada y Salida

Lectura y escritura de archivos, manejo de errores con `try/except`.

---

## Temas

- `open`, `readline`, `readlines`, `read`
- Modos de apertura: `r`, `w`, `a`
- `close` y contexto `with`
- Archivos CSV
- Manejo de errores: `try`, `except`, `finally`
- Validación de entrada del usuario

---

## Ejercicios

### Archivos

| N° | Descripción |
|---|---|
| 1 | `contar`: cantidad de filas de un archivo |
| 2 | `imprimir`: mostrar contenido, opción ignorar líneas vacías |
| 3 | `ver_encabezado`: primeras N líneas |
| 4 | `ver_final`: últimas N líneas |
| 5 | `crear`: crear o limpiar un archivo |
| 6 | `wc`: contar líneas, palabras y caracteres |
| 7 | `grep`: líneas que contienen una cadena |
| 8 | Leer pregunta de archivo y guardar respuesta |
| 9 | `guardar_diccionario` / `cargar_diccionario` en CSV |
| 10 | ⭐ Desafío: dividir archivo grande en partes de 50 líneas |
| 11 | Detector de plagio: reporte de apariciones de una palabra |
| 12 | Reemplazar palabra en un archivo |
| 13 | Gestor de tareas pendientes / completadas |
| 14 | Combinar dos archivos en un CSV `sala;pelicula` |
| 15 | Precio promedio de un producto en ventas CSV |
| 16 | Primeras 5 líneas de una lista de archivos |
| 17 | ⭐ Desafío: detector de ejercicios con más de 5 líneas |
| 18 | ⭐ Desafío: extractor de secciones de apuntes |

### Manejo de Errores

| N° | Descripción |
|---|---|
| 1 | Apertura segura de archivo |
| 2 | Suma de 5 números con validación de entrada |
| 3 | Par/impar con validación, termina con `*` |
| 4 | Temperatura promedio ignorando valores inválidos |
| 5 | División de pares de números desde archivo |
| 6 | Reserva de butacas con validación |
| 7 | ⭐ Desafío: función `dividir` con manejo de `ZeroDivisionError` |
| 8 | Desafío: kiosco con menú y validación de entrada |
| EC | Evaluación de código: identificar y corregir errores |

---

## Archivos

```
guia_05/
├── ejercicios.py
├── datos/           ← archivos .txt y .csv usados en los ejercicios
└── salidas/         ← archivos generados al ejecutar los scripts
```

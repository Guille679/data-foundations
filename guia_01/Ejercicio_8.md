## Ejercicio 8 — Algoritmo para organizar libros en una biblioteca

**EJERCICIO DADO**
Una biblioteca quiere organizar sus libros en estantes. Cada libro tiene: título, autor, género (novela, ciencia, historia, etc.) y año de publicación. Los estantes tienen capacidad limitada. Describí un algoritmo para decidir en qué estante va cada libro, considerando que queremos que sea fácil encontrarlos después.

**Objetivo:** Clasificar y ubicar libros en estantes de capacidad limitada para optimizar la búsqueda posterior.


**Elementos necesarios:**

**DATOS DEL LIBRO (Entrada)**
Para que un libro sea rastreable, necesitamos su "metadato":

- Título y Autor: Identificación unívoca.
- Género: (Novela, Ciencia, Historia) El criterio principal de agrupación.
- Año de publicación: Para orden cronológico dentro de un mismo tema.

**DATOS DEL ESTANTE (Logística)**
- ID de Estante: Ubicación física.
- Categoría asignada: Género que admite ese estante.
- Capacidad Máxima: Cantidad de ejemplares que soporta antes de llenarse.

**Pasos:**
1. Clasificación Primaria: Agrupar los libros por Género. Cada género tendrá su sector de estantes asignado.
2. Ordenamiento Secundario: Dentro de cada grupo de género, ordenar los libros alfabéticamente por Autor (o por Año si es una colección técnica).
3. Para cada libro (en el orden definido en el paso 2):
   a. Identificar el estante asignado a su género.
   b. Verificar si el estante tiene capacidad > 0.
   c. Si tiene espacio: colocar el libro, descontar 1 de la capacidad, registrar ubicación.
   d. Si no tiene espacio: habilitar estante de continuidad y repetir desde b.
4. Continuar hasta procesar todos los libros.
5. Excepción (Desborde): Si el estante está lleno, habilitar un "Estante de Continuidad" con la misma etiqueta de género.
6. Registro de Ubicación: Generar un índice (físico o digital) que indique en qué estante quedó cada título. 
## Ejercicio 6 — Recorrido óptimo en un supermercado

**EJERCICIO DADO**
Contás con un listado de cosas a comprar y tenés que ir a un supermercado que cuenta con distintas góndolas o pasillos. Cada góndola o pasillo puede contar con varios, uno o ninguno de los productos de tu lista. ¿Cuál sería el listado de instrucciones para poder terminar lo más rápido posible?

**Objetivo:** Organizar una lista de compras dispersa para completar el recorrido del supermercado en el menor tiempo posible, evitando retrocesos.

**Elementos necesarios:**

**DATOS DE ENTRADA (La Lista)**
- Para que el proceso sea rápido, primero necesitamos saber qué buscamos.
- Lista de artículos: Los productos deseados.
- Mapa de góndolas: Ubicación de las categorías (Lácteos, Limpieza, Carnicería, etc.).

**DATOS DE PROCESAMIENTO (La Estrategia)**
- Categorización: Agrupar productos que están en el mismo pasillo.
- Ruta Lineal: Ordenar las categorías según la entrada y la salida del local.
- Prioridad de Frío: Dejar productos congelados o frescos para el final de la lista.


**Pasos:**
1. Clasificar la lista por góndola antes de entrar.
2. Ordenar las góndolas según la ruta del local (entrada → salida), dejando frescos y congelados para el final.
3. Ir a la primera góndola de la ruta.
4. Para cada producto asignado a esa góndola:
   a. Buscar el producto en la góndola.
   b. Si está disponible: tomarlo y marcarlo como completado.
   c. Si no está: decidir reemplazo o descarte y continuar.
5. Si quedan góndolas por recorrer, avanzar a la siguiente y repetir desde paso 4.
6. Al terminar todas las góndolas, dirigirse a la caja con menor espera.
7. Pagar y recibir el ticket.


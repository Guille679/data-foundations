## Ejercicio 10 — Asignación de pedidos a repartidores

**EJERCICIO DADO** 
Una aplicación de delivery necesita asignar pedidos a repartidores. Cada pedido tiene: dirección de entrega, hora límite de entrega y tipo de producto (comida caliente, bebidas, productos frágiles). Cada repartidor tiene: ubicación actual, tipo de vehículo (bicicleta, moto, auto) y pedidos ya asignados. Describí qué criterios usarías para decidir qué repartidor debe tomar cada pedido nuevo.

**Objetivo:** Vincular un pedido entrante con el repartidor más apto para garantizar una entrega rápida y en buen estado.

**Elementos necesarios:**

**DATOS DEL PEDIDO (Variables de Entrada)**

Para priorizar la asignación, el sistema analiza:

- Tipo de Producto: (Caliente, Frágil, Bebida) Define el cuidado y la velocidad.
- Hora Límite: El "deadline" para evitar que la comida se enfríe o llegue tarde.
- Dirección de Entrega: Coordenadas de destino.

**DATOS DEL REPARTIDOR (Recursos Disponibles)**
- Ubicación Actual: Para calcular el tiempo de llegada al local.
- Tipo de Vehículo: (Bici para distancias cortas, Moto/Auto para largas o pedidos pesados).
- Carga de Trabajo: Cantidad de pedidos activos para no saturarlo.

**Pasos:**
1. Filtrado por Disponibilidad: Identificar qué repartidores están activos y tienen menos de X pedidos asignados.
2. Validación de Vehículo: Si el producto es frágil o voluminoso, descartar bicicletas y priorizar autos. Si es comida caliente, priorizar motos por su agilidad en tráfico.
3. De los repartidores que pasaron los filtros anteriores, ordenarlos por distancia al local de origen (de menor a mayor) y tomar los primeros 3 como candidatos.
4. Estimación de Tiempo: Sumar el tiempo de retiro + el tiempo de viaje al destino. Verificar que el total sea menor a la Hora Límite.
5. Asignación Final: Notificar al repartidor con el mejor puntaje de cercanía y tiempo.
6. Confirmación de Recepción: Si el repartidor rechaza, el sistema ejecuta el paso 5 con el siguiente candidato en la lista.


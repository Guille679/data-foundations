## Ejercicio 3 — Colecta de alimentos en CABA

**EJERCICIO DADO**
Se te pide que organices una colecta de alimentos no perecederos por la Ciudad de Buenos Aires. Contamos con algunos automóviles y camionetas de voluntarios, un listado de donaciones, listado de los alimentos a donar, la disponibilidad horaria y la dirección en la cual se dejan los alimentos. La colecta se realiza en un solo día. ¿Cómo la organizarías?

**Objetivo:** Coordinar el retiro y entrega de donaciones en un solo día utilizando una flota de voluntarios.

**Elementos necesarios:**
- Flota: Automóviles (donaciones pequeñas) y camionetas (donaciones grandes).
- Base de datos: Listado de donantes, direcciones y horarios de disponibilidad.
- Centro de recepción: Dirección final donde se descargan los alimentos.
- Mapa de CABA: Dividido por zonas (Norte, Sur, Centro, Oeste).
- Comunicación: Teléfono o radio para coordinar a los voluntarios. 

**Pasos:**
1. Clasificar las donaciones por volumen para asignar un automóvil o una camioneta según el tamaño de la carga.
2. Agrupar las direcciones de retiro por barrios o cercanía geográfica para crear "zonas de recolección".
3. Para cada zona, verificar si algún donante tiene restricción horaria. Si la tiene, ajustar el orden de visitas para cumplir ese horario primero.
4. Trazar la ruta óptima para cada conductor, iniciando en el punto más lejano y terminando en el centro de recepción.
5. Entregar a cada voluntario su hoja de ruta con nombres, direcciones, horarios y teléfono de contacto del donante.
6. Iniciar el recorrido de recolección en el horario pactado.
7. Si un vehículo reporta demora mayor a 30 minutos, reasignar sus próximas paradas al vehículo disponible más cercano.
8. Dirigir todos los vehículos al centro de recepción una vez completada su ruta.
9. Descargar y contabilizar los alimentos no perecederos recibidos.
10. Finalizar la jornada con el cierre del centro de recepción.

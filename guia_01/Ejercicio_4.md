## Ejercicio 4 — Invitaciones Personalizadas

**EJERCICIO DADO**
Tenés que enviar invitaciones personalizadas para tu cumpleaños. Cada invitación tiene que mencionar el nombre de la persona y la cantidad de invitados adicionales con los que puede venir. Contamos con una impresora a la que le das el texto a enviar, un listado con los nombres de los invitados y los invitados adicionales que pueden ellos traer. ¿Cómo redactarías el texto de la invitación?

**Objetivo:** Generar un texto base que se adapte automáticamente a cada invitado de la lista antes de mandarlo a la impresora.

**Elementos necesarios:**
- Listado de datos: Nombres y número de acompañantes permitidos.
- Plantilla de texto: El cuerpo del mensaje con "huecos" para la información.
- Impresora: El dispositivo de salida que recibirá el texto final.

**Pasos:**
1. Definir el texto base de la invitación dejando espacios claros para los datos variables (ejemplo: "Hola [Nombre]...").
2. Tomar el primer registro de la lista de invitados.
3. Identificar el nombre de la persona en ese registro.
4. Identificar la cantidad de acompañantes permitidos para esa persona.
5. Reemplazar la etiqueta "[Nombre]" en la plantilla por el nombre real del invitado.
6. Reemplazar la etiqueta "[Cantidad]" en la plantilla por el número de invitados adicionales.
7. Enviar el texto resultante (ya personalizado) a la cola de impresión.
8. Verificar si quedan más nombres en el listado.
9. Repetir desde el paso 2 hasta que se agote la lista de invitados.
10. Finalizar el proceso de impresión una vez procesado el último nombre.

# Ejercicio 6 - Sistema de estudiantes FIUBA

# EJERCICIO DADO -- Nos contratan para hacer un nuevo sistema de FIUBA para almacenar información de sus estudiantes:

# nombre	apellido   dni	    carrera
# Violeta	Perez	  42000000	Informática
# Carla	    Guanca	  42001001	Mecánica
# Manuela	Gomez	  42002002	Química

# Crear un diccionario que sirva para representar a cada persona. 
# Debe contener las claves nombre, apellido, dni y carrera. Los diccionarios se deben guardan en una lista llamada estudiantes.

# Agregar al diccionario creado un nuevo elemento, que debe ser otro diccionario y represente las notas obtenidas en la carrera. 
# La clave debe ser el codigo y el valor la nota (del 1 al 10) obtenida.

# Crear código que agregue para la estudiante Violeta Perez la nota 7 en la materia Algoritmos y Programación III (7507), y la nota 4 en la materia Análisis Matemático II (6103).

# Teniendo la lista de estudiantes, buscar en la lista la persona con mayor cantidad de notas e imprimirla por pantalla.

# 1) Crear los diccionarios y la lista
estudiantes = [
    {"nombre": "Violeta", "apellido": "Perez", "dni": 42000000, "carrera": "Informatica"},
    {"nombre": "Carla", "apellido": "Guanca", "dni": 42001001, "carrera": "Mecanica"},
    {"nombre": "Manuela", "apellido": "Gomez", "dni": 42002002, "carrera": "Quimica"}
]

# 2) Agregar el diccionario de notas a cada estudiante
for estudiante in estudiantes:
    estudiante["notas"] = {}

# 3) Agregar notas especificas a Violeta Perez
for estudiante in estudiantes:
    if estudiante["nombre"] == "Violeta" and estudiante["apellido"] == "Perez":
        estudiante["notas"]["7507"] = 7
        estudiante["notas"]["6103"] = 4

# 4) Buscar la persona con mayor cantidad de notas
estudiante_con_mas_notas = estudiantes[0]

for estudiante in estudiantes:
    # Comparar la cantidad de elementos en el diccionario de notas
    if len(estudiante["notas"]) > len(estudiante_con_mas_notas["notas"]):
        estudiante_con_mas_notas = estudiante

# Imprimir el resultado
print("Estudiante con mayor cantidad de notas:")
print(estudiante_con_mas_notas)

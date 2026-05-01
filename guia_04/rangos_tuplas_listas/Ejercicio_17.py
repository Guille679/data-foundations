# Ejercicio 17 - Desafío: agenda con búsqueda parcial

# EJERCICIO DADO -- Desafio (no obligatorio): Agenda Simplificada
# Escribir una función que reciba una cadena a buscar y una lista de tuplas (nombre_completo, telefono),
# y busque dentro de la lista todas las entradas que contengan en el nombre completo la cadena recibida 
# (puede ser el nombre, el apellido o sólo una parte de cualquiera de ellos). Debe devolver una lista con todas las tuplas encontradas.


def buscar_en_agenda(busqueda, lista_agenda):
    resultado = []
    busqueda_min = busqueda.lower()

    for nombre, telefono in lista_agenda:
        nombre_min = nombre.lower()

        if busqueda_min in nombre_min:
            resultado.append((nombre, telefono))

    return resultado

# Ejemplo de uso
agenda = [
    ("Juan Perez", "123456"),
    ("Ana Gomez", "987654"),
    ("Mariana Lopez", "555666")
]

# Buscara cualquier nombre que contenga "ana"
busqueda = "ana"
encontrados = buscar_en_agenda(busqueda, agenda)

print("Contactos encontrados:")
for contacto in encontrados:
    print(contacto)

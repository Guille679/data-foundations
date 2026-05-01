# Ejercicio 7 - Vivero: agregar plantas a una lista de diccionarios

# EJERCICIO DADO -- En un vivero se guardan las plantas en una lista de diccionarios con la siguiente información: 
# especie, luz directa (si/no), precio. Se necesita un sistema que guarde las plantas a medida que van llegando. 
# Hacer una función que reciba la lista de diccionarios de plantas, y los datos de la planta nueva, y agregue esa planta a la lista de diccionarios.

def agregar_planta(lista_vivero, especie, luz_directa, precio):
    nueva_planta = {
        "especie": especie,
        "luz_directa": luz_directa,
        "precio": precio
    }
    lista_vivero.append(nueva_planta)

# Ejemplo de uso
vivero = []

agregar_planta(vivero, "Helecho", "no", 1500)
agregar_planta(vivero, "Cactus", "si", 800)
agregar_planta(vivero, "Rosa", "si", 2200)

print("Inventario del vivero:")
for planta in vivero:
    print(planta)

# Ejercicio 4 - Lista de tuplas: países y mundiales

# EJERCICIO DADO -- Dada la lista de tuplas [("Argentina", 3), ("España",1), ("Uruguay", 2), ("Francia",2)], donde cada tupla contiene un país y la cantidad de mundiales que ganaron:

# Hacer una función que reciba la lista por parámetro e imprima la información de cada país con el siguiente formato:
# País: <nombre> - Copas: <cantidad>
# Si y sólo si el país es “Argentina”, se debe imprimir el nombre con 3 estrellas: "Argentina⭐⭐⭐". Usar el operador abreviado +=.

# Hacer una función que reciba la lista por parámetro y devuelva la cantidad de mundiales que ganaron entre todos los países. Ejemplo: contar_mundiales([("Argentina", 3), ("España",1), ("Uruguay", 2), ("Francia",2)]) debe devolver 8.

# Hacer una función que reciba la lista por parámetro y la devuelva, ordenada por cantidad de copas ganadas.

# Hacer una función que reciba la lista por parámetro y devuelva en una tupla: una lista con los países que tienen más de una copa ganada, y otra lista con valores booleanos que nos diga si la cantidad de copas es par o impar. Pista: ¿Cómo podemos usar filter? ¿Y map?
# Ejemplo: [("Argentina", 3), ("España",1), ("Uruguay", 2), ("Francia",2)] devuelve:
# ([("Argentina", 3), ("Uruguay", 2), ("Francia",2)] , [False, True, True])


# Primera parte

def mostrar_paises(lista):
    for pais, copas in lista:
        nombre_mostrar = pais
        if nombre_mostrar == "Argentina":
            nombre_mostrar += "⭐⭐⭐"
        print("Pais: " + nombre_mostrar + " - Copas: " + str(copas))

# Segunda parte

def contar_mundiales(lista):
    total = 0
    for pais, copas in lista:
        total += copas
    return total

# Tercera parte

def ordenar_por_copas(lista):
    # sorted devuelve una lista nueva ordenada por el segundo elemento (copas)
    return sorted(lista, key=lambda x: x[1])

# Cuarta parte

def procesar_datos(lista):
    # Filtrar las tuplas donde la posicion [1] es mayor a 1
    lista_mas_de_una = [pais for pais in lista if pais[1] > 1]

    # Mapear la paridad de la posicion [1] de cada tupla
    lista_paridad = [pais[1] % 2 == 0 for pais in lista]
    
    return (lista_mas_de_una, lista_paridad)

# Ejemplos de uso

mundiales = [("Argentina", 3), ("España", 1), ("Uruguay", 2), ("Francia", 2)]

print("--- Informacion de paises ---")
mostrar_paises(mundiales)

print("\nTotal de mundiales:", contar_mundiales(mundiales))

print("\nOrdenados por copas:", ordenar_por_copas(mundiales))

datos_procesados = procesar_datos(mundiales)
print("\nMas de una copa y paridad:", datos_procesados)

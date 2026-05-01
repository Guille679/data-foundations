# Ejercicio 11 - Acceso a elemento de una matriz por tupla (fila, columna)

# EJERCICIO DADO -- Escribir una función que reciba una matriz y una tupla (fila, columna), y devuelva el valor ubicado en esa posición de la matriz.

def obtener_valor(matriz, posicion):
    fila = posicion[0]
    columna = posicion[1]

    valor = matriz[fila][columna]

    return valor

# Ejemplo de uso

mi_matriz = [
    [10, 20, 30], # Fila 0
    [40, 50, 60], # Fila 1
    [70, 80, 90]  # Fila 2
]

# Queremos el valor 60, que esta en la fila 1, columna 2
ubicacion = (1, 2)

resultado = obtener_valor(mi_matriz, ubicacion)
print("El valor en la posicion", ubicacion, "es:", resultado)

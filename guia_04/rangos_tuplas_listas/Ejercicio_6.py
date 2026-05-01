# Ejercicio 6 - Producto escalar de dos vectores

# EJERCICIO DADO -- Escribir una función que reciba dos vectores y devuelva su prod_escalar.

def calcular_producto_escalar(vector1, vector2):
    resultado = 0
    largo = len(vector1)

    for i in range(largo):
        multiplicacion = vector1[i] * vector2[i]
        resultado = resultado + multiplicacion
    
    return resultado

# Ejemplo de uso

v1 = [1, 2, 3]
v2 = [4, 5, 6]

print("El producto escalar es:", calcular_producto_escalar(v1, v2))

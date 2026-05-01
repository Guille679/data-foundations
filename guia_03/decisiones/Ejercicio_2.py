# Ejercicio 2 - Función: implementación propia de `abs`

# EJERCICIO DADO -- Escribir una implementación propia de la función abs, 
# que devuelva el valor absoluto de cualquier valor que reciba. 
# Ejemplo: mi_abs(5) devuelve 5 y mi_abs(-5) devuelve 5.


# El valor absoluto de un número es simplemente su distancia respeto al cero, sin importar su signo.
# es decir, si el numero es positivo, se queda igual; si es negativo, le quitamos el menos (lo multiplicamos por -1).

def mi_abs(n):
    if (n < 0):
        return n * -1
    else:
        return n

# Ejemplos de uso corregidos:
resultado1 = mi_abs(-10)
print(f"El absoluto de -10 es: {resultado1}")

resultado2 = mi_abs(5)
print("El absoluto de 5 es:", resultado2)

# Ejemplo con operación matemática
suma = mi_abs(-5) + mi_abs(-5)
print(f"La suma de los absolutos es: {suma}")

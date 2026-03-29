# Ejercicio 19 - Función: norma de un vector en R³ 

# EJERCICIO DADO -- Escribir una función que calcule la norma de un vector en R³ recibiendo como parámetros las 3 componentes v1, v2, v3 del mismo.

import math

def calcular_norma_r3(v1, v2, v3):

    # Sumar los cuadrados de las componentes
    suma_cuadrados = v1**2 + v2**2 + v3**2
    
    # Calcular la raíz cuadrada
    norma = math.sqrt(suma_cuadrados)
    return norma

# Ejemplo de uso: vector (3, 2, 6)
resultado = calcular_norma_r3(3, 2, 6)
print(f"La norma del vector es: {resultado}") # Debería dar 7.0


# Ejercicio 11 - Función: devolver resto y cociente  

# EJERCICIO DADO -- Crear una función que reciba dos enteros y que devuelva el resto y el cociente entre ellos.

def calcular_division(dividendo, divisor):
    cociente = dividendo // divisor 
    resto = dividendo % divisor
    return cociente, resto


# Ejemplos de uso

# Para 10 dividido entre 3, el cociente es 3 y el resto es 1
print(calcular_division(10, 3)) 
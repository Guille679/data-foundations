# Ejercicio 1 - Función: detectar si un número es impar

# EJERCICIO DADO -- Escribir una función que, dado un número entero n, calcule si es impar o no.

def es_impar(n):
    if (n % 2 != 0):
        print(f"El número {n} es IMPAR")
    else:
        print(f"El número {n} es PAR")

# Ejemplo de uso:

numero_usuario = int(input("Escribe un número: "))
es_impar(numero_usuario)
    

    
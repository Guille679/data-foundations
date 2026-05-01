# Ejercicio 3 - Función: detectar si un número es entero

# EJERCICIO DADO -- Escribir una función que reciba un número y devuelva True si es entero y False si no lo es. no se puede usar la función isinstance.


# Para saber si un número es entero sin usar funciones de tipo, podemos comparar el número original con su version truncada (parte entera).

# Para averiguar su parte truncada podemos usar el operador módulo porque si dividimos cualquier numero entero por 1, el residuo sera siempre 0.
# pero si el número tiene decimales, al dividirlo por 1, el residuo justamente sera esa parte decimal.

# 10 / 1 --> 0 (entero)
# 7.5 / 1 --> 0.5 (no es entero)
# 4.0 / 1 --> 0 (entero)


def es_entero_con_residuo(n):
    if (n % 1 == 0):
        return True
    else:
        return False

# Ejemplos de uso:

resultado1 = es_entero_con_residuo(10)
print(f"El numero 10 es entero: {resultado1}") # Muestra True

resultado2 = es_entero_con_residuo(7.5)
print(f"El numero 7.5 no es entero: {resultado2}") # Muestra False

resultado3 = es_entero_con_residuo(0)
print(f"El numero 0 es entero: {resultado3}") # Muestra True
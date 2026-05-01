# Ejercicio 10 - Lista de 1 a N

# EJERCICIO DADO -- Escribir una función que dado un valor n, devuelva una lista con los números del 1 a n 

def generar_lista(n):
    # Usar n + 1 para que incluya al numero n
    lista_resultado = list(range(1, n + 1))
    return lista_resultado

# Ejemplo de uso

numero = 5
resultado = generar_lista(numero)

print("La lista generada es:", resultado)
# Si numero es 5, devuelve [1, 2, 3, 4, 5]

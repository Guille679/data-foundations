# Ejercicio 10 -  ⭐ Desafío: imprimir primos entre 1 y N

# EJERCICIO DADO -- Desafío (obligatorio): Crear una función que reciba un número entero e imprima los números primos entre 1 y el número ingresado.

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def mostrar_primos_hasta(limite):
    print(f"Numeros primos entre 1 y {limite}:")
    for n in range(1, limite + 1):
        if es_primo(n):
            print(n, end=" ") # El end=" " sirve para que salgan uno al lado del otro
    print() # Salto de línea

# Ejemplo de uso:
num_usuario = int(input("Ingrese un numero máximo: "))
mostrar_primos_hasta(num_usuario)

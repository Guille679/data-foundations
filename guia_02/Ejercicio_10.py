# Ejercicio 10 - Función: concatenar número y string

# EJERCICIO DADO -- Crear una función que reciba un número y un string, y que devuelva ambos concatenados dentro de un nuevo string.

def concatenar_datos(numero, texto):
    return str(numero) + texto

# Ejemplos de uso

# Ejemplo 1: Guardando el resultado en una variable
union = concatenar_datos(24, " de Marzo")
print(f"La fecha es: {union}")

# Ejemplo 2: Usando los valores directamente en el print
print(f"Resultado directo: {concatenar_datos(10, ' es un número')}")

# Ejemplo 3: Con datos ingresados por el usuario
n = int(input("Ingresa un número: "))
t = input("Ingresa un texto: ")
print(f"Tu unión es: {concatenar_datos(n, t)}")
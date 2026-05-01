# Ejercicio 5 -  Programa: tablas de multiplicar con salida por "X"

# EJERCICIO DADO -- Escribir un programa que le pida al usuario que ingrese un número. 
# Para ese número, se imprime la tabla de multiplicar del 1 al 10. Luego, se le vuelve a pedir otro número. 
# Si el usuario ingresa “X”, el programa debe terminar. El usuario debe poder ingresar números indefinidamente hasta que ingrese “X”.

# jemplo:

# Hola! Esto es Tablas de Multiplicar
# Ingrese un número o "X" para salir: 1
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 1 x 4 = 4
# 1 x 5 = 5
# 1 x 6 = 6
# 1 x 7 = 7
# 1 x 8 = 8
# 1 x 9 = 9
# 1 x 10 = 10
# Ingrese un número o "X" para salir: -2
# Error: El número debe ser positivo y estar entre 1 y 10
# Ingrese un número o "X" para salir: X
# ¡Adios!


def generar_tabla(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

print("¡Hola! Esto es Tablas de Multiplicar")

while True:
    entrada = input('Ingrese un numero o "X" para salir: ')

    # 1. Verificar si quiere salir
    if entrada.upper() == "X":
        print("¡Adiós!")
        break # Cortar el bucle while
    
    # 2. Intentar convertir a numero y validar
    num = int(entrada)
    
    if 1 <= num <= 10:
        generar_tabla(num)
    else:
        print("Error: El número debe ser positivo y estar entre 1 y 10")

# Ejercicio 7 -  Juego: adivinar un número (con límite de intentos y `random`)

# EJERCICIO DADO -- Hacer una función que reciba un número del 1 al 10, y luego permita al usuario poder adivinar ese número, 
# ingresando valores repetidamente. Para cada ingreso del usuario, el programa debe indicarle si su número es menor o mayor al número a adivinar.
# Una vez que el usuario ingresa el número correcto, lo felicita y termina.

# Repetir permitiendo únicamente 3 intentos.

# Repetir generando el número aleatoriamente de la siguiente forma dentro de la función, sin recibirlo por parámetro:

# import random
# numero_a_adivinar = random.randint(1, 10)
# print(numero_a_adivinar)

import random 

# 1. Adivinar con intentos infinitos 
def adivinar_basico(numero_secreto):
    print("¡Adivina el numero secreto!")
    acerto = False

    while not acerto:
        intento = int(input("Ingrese el numero: "))
    
        if intento == numero_secreto:
            print("¡Felicitaciones! Acertaste.")
            acerto = True
        elif intento < numero_secreto:
            print("El número a adivinar es mayor.")
        else:
            print("El número a adivinar es menor.")

# 2. Adivinar con limite de 3 intentos
def adivinar_con_limite(numero_secreto):
    intentos_maximos = 3
    intentos_actual = 0
    gano = False

    while intentos_actual < intentos_maximos and not gano:
        intentos_actual += 1
        # Usar f-string para evitar el error de concatenación
        num_usuario = int(input(f"Intento {intentos_actual}. Ingresa un numero: "))

        if num_usuario == numero_secreto:
            print("¡Felicitaciones!, Ganaste.")
            gano = True
        elif num_usuario < numero_secreto:
            print("Es mas grande")
        else:
            print("Es mas chico")

    if not gano:
        print(f"Te quedaste sin intentos. El numero era: {numero_secreto}")

# 3. Adivinar con numero al azar (La más prolija)
def adivinar_azar_completo():
    numero_secreto = random.randint(1, 10)
    intentos = 3
    acierto = False

    for i in range(1, intentos + 1):
        jugada = int(input(f"Intento {i}: ¿Que numero es? "))
        
        if jugada == numero_secreto:
            print("¡Increible! Lo lograste :)")
            acierto = True
            break
        elif jugada < numero_secreto:
            print("Pista: El secreto es mayor")
        else:
            print("Pista: El secreto es menor")
            
    if not acierto:
        print(f"Perdiste. El numero era el {numero_secreto}")

# Ejemplos de uso
adivinar_basico(7)
adivinar_con_limite(5)
adivinar_azar_completo()

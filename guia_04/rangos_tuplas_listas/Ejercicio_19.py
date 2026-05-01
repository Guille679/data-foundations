# Ejercicio 19 - Desafío: Batalla Naval

# EJERCICIO DADO -- Super Desafio (no obligatorio): Batalla Naval

# Se tiene una matriz de 10x10 que representa un tablero. Cada celda contiene un 0 si está vacía, o un 1 si hay un barco (consideramos que en este caso, sólo hay barcos unitarios que ocupan un espacio).

# La posición de los barcos se representa con tuplas de (fila, columna). Por ejemplo, si se tiene un barco en la fila 1, columna 3, se representa con la tupla (1, 3).

# Escribir una función que cree un tablero con 10 barcos ubicados aleatoriamente (usar la biblioteca random), y que permita al usuario intentar adivinar dónde están.

# El usuario luego ingresa una posición, y la máquina indica si había un barco en esa posición (mostrando un mensaje por pantalla “¡Hundido!”) o no (“¡Agua!”).

# El usuario gana cuando hunde todos los barcos del tablero. Si se equivoca más de 5 veces, pierde.

import random

def jugar_batalla_naval():
    tablero = []
    for i in range(10):
        tablero.append([0] * 10)

    barcos_colocados = 0
    while barcos_colocados < 10:
        fila = random.randint(0, 9)
        columna = random.randint(0, 9)
        
        if tablero[fila][columna] == 0:
            tablero[fila][columna] = 1
            barcos_colocados += 1

    aciertos = 0
    errores = 0
    max_errores = 5
    barcos_totales = 10

    print("--- BIENVENIDO A BATALLA NAVAL ---")
    print(f"Hay {barcos_totales} barcos ocultos. Puedes fallar hasta {max_errores} veces.")

    while aciertos < barcos_totales and errores < max_errores:
        print(f"\nAciertos: {aciertos} | Errores: {errores}/{max_errores}")
        
        try:
            f_tiro = int(input("Ingresa fila (0-9): "))
            c_tiro = int(input("Ingresa columna (0-9): "))
            
            if not (0 <= f_tiro <= 9 and 0 <= c_tiro <= 9):
                print("Coordenadas fuera de rango. Prueba del 0 al 9.")
                continue
                
            if tablero[f_tiro][c_tiro] == 1:
                print("¡HUNDIDO!")
                tablero[f_tiro][c_tiro] = 0 
                aciertos += 1
            else:
                print("¡AGUA!")
                errores += 1
                
        except ValueError:
            print("Por favor, ingresa solo numeros.")

    if aciertos == barcos_totales:
        print("\n¡FELICITACIONES! Hundiste toda la flota.")
    else:
        print("\nGAME OVER. Te quedaste sin intentos.")
        print("Los barcos restantes estaban en:")
        for r in range(10):
            for c in range(10):
                if tablero[r][c] == 1:
                    print(f"Fila {r}, Columna {c}")

# Ejecutar el juego
if __name__ == "__main__":
    jugar_batalla_naval()

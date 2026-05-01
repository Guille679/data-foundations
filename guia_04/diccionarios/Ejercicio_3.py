# Ejercicio 3 - Simulación de dados con `random`

# EJERCICIO DADO -- Escribir una función que reciba una cantidad de iteraciones N.

# Se deberá simular una persona que tira un dado N veces, y se deberá devolver un diccionario con la cantidad de apariciones de cada valor en el dado. 
# Nota: para simular una tirada, usar import random y random.randint(1, 6).

# Repetir el punto anterior, si ahora en vez de tirar 1 dado, tira 2. 
# Se debe devolver un diccionario con la cantidad de apariciones de cada valor de la suma de ambos dados.

import random

def SimularDado(N):
    resultados = {}

    for _ in range(N):
        tirada = random.randint(1, 6)
        
        if tirada in resultados:
            resultados[tirada] += 1
        else:
            resultados[tirada] = 1
            
    return resultados


def SimularDosDados(N):
    resultado_suma = {}

    for _ in range(N):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        suma = dado1 + dado2

        if suma in resultado_suma:
            resultado_suma[suma] += 1
        else:
            resultado_suma[suma] = 1
            
    return resultado_suma

# Ejemplo de uso
N = 100
print("Frecuencia de un dado:", SimularDado(N))
print("Frecuencia suma de dos dados:", SimularDosDados(N))

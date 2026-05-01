# Ejercicio 15 - ⭐ Desafío: matriz identidad de tamaño N

# EJERCICIO DADO -- Desafio (obligatorio): Escribir una función que reciba un tamaño y devuelva una matriz con 1 en la diagonal principal y 0 en el resto.

def crear_matriz_identidad(tamano):
    matriz_final = []

    for i in range(tamano):
        fila_actual = []
        for j in range(tamano):
            if i == j:
                fila_actual.append(1)
            else:
                fila_actual.append(0)
        
        matriz_final.append(fila_actual)

    return matriz_final

# Ejemplo de uso
n = 3
identidad = crear_matriz_identidad(n)

print("Matriz Identidad:")
for fila in identidad:
    print(fila)

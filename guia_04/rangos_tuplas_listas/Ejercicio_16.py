# Ejercicio 16 - ⭐ Desafío: transpuesta de una matriz

# EJERCICIO DADO -- Desafio (obligatorio): Escribir una función que reciba una matriz y devuelva su transpuesta. 
# Ejemplo: si recibe la matriz [[1, 2, 3], [4, 5, 6]], debe devolver [[1, 4], [2, 5], [3, 6]].

def transponer_matriz(matriz):
    # 1. Obtener dimensiones originales
    cant_filas_orig = len(matriz)
    cant_cols_orig = len(matriz[0])
    
    # 2. Inicializar la matriz transpuesta vacia
    matriz_transpuesta = []
    
    # 3. Ciclos para transponer (filas x columnas)
    for j in range(cant_cols_orig):
        nueva_fila = []
        for i in range(cant_filas_orig):
            valor = matriz[i][j]
            nueva_fila.append(valor)
        matriz_transpuesta.append(nueva_fila)
        
    return matriz_transpuesta

# Ejemplo de uso
matriz_original = [
    [1, 2, 3],
    [4, 5, 6]
]

# Resultado esperado:
# [
#   [1, 4],
#   [2, 5],
#   [3, 6]
# ]

resultado = transponer_matriz(matriz_original)
print(resultado)

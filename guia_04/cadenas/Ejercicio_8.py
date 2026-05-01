# Ejercicio 8 - ⭐ Desafío: buscador de ocurrencias en un texto

# EJERCICIO DADO -- Desafío (obligatorio):

# Se quiere implementar un buscador dentro de un editor de texto, que permita encontrar todas las ocurrencias de una palabra en un texto. 
# Para ello, se debe implementar una función que reciba como parámetro una palabra y un texto, y que devuelva la primer aparición de la palabra en el texto.

# Modificar la función anterior para que devuelva una lista con las posiciones de inicio de cada ocurrencia de la palabra dentro del texto. 

# Modificar la función anterior para que devuelva la cantidad de ocurrencias encontradas. Restricción: No se puede usar el método len.


# Primera parte
def BuscarPrimero(palabra, texto):
    return texto.find(palabra)

# Segunda parte
def BuscarTodas(palabra, texto):
    posiciones = []
    actual = texto.find(palabra)
    while actual != -1:
        posiciones.append(actual)
        actual = texto.find(palabra, actual + 1)
    return posiciones

# Tercera parte
def ContarOcurrencias(palabra, texto):
    posiciones = BuscarTodas(palabra, texto)
    contador = 0
    for _ in posiciones:
        contador += 1
    return contador


# Ejemplos de uso

texto_ejemplo = "el sol brilla fuerte, porque el sol es una estrella"
palabra_a_buscar = "sol"

# 1. Primera aparicion
primera = BuscarPrimero(palabra_a_buscar, texto_ejemplo)
print(f"Primera aparicion en el indice: {primera}") 
# Resultado: 3

# 2. Todas las posiciones
todas = BuscarTodas(palabra_a_buscar, texto_ejemplo)
print(f"Lista de posiciones: {todas}") 
# Resultado: [3, 32]

# 3. Cantidad total (sin usar len)
total = ContarOcurrencias(palabra_a_buscar, texto_ejemplo)
print(f"Cantidad de veces encontrada: {total}") 
# Resultado: 2



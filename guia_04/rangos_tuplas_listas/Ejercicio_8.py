# Ejercicio 8 - Últimos N elementos en orden inverso

# EJERCICIO DADO -- Escribir una función que reciba una lista y un número n
# para dicho número n debe imprimir los últimos n elementos de la lista en orden inverso, y luego devolver la lista sin ellos. 
# Ejemplo: Si se recibe [1, 2, 3, 4, 5] y n = 2, debe imprimir 5, 4 y devolver [1, 2, 3].

def procesar_lista(lista, n):
    # 1. Obtener y revertir los ultimos n elementos usando slicing negativo
    # Si n=0, lista[-0:] daria la lista completa, manejamos ese caso
    if n <= 0:
        return lista
        
    ultimos_invertidos = lista[-n:][::-1]
    
    # 2. Imprimirlos
    for elemento in ultimos_invertidos:
        print(elemento)
        
    # 3. Devolver la lista sin los ultimos n
    return lista[:-n]

# Ejemplo de uso 
mi_lista = [1, 2, 3, 4, 5]
cantidad = 2

resultado = procesar_lista(mi_lista, cantidad)
print("Lista resultante:", resultado)

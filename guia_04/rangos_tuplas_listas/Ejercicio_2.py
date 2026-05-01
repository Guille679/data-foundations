# Ejercicio 2 - Funciones sobre listas: longitud par, máximo/mínimo, ordenar

# EJERCICIO DADO -- Escribir una función que reciba:

# Una lista y devuelva True si su longitud es par y False si su longitud es impar.
# Una lista de números cualesquiera y devuelva el elemento máximo y el mínimo.
# Una lista de números y devuelva otra lista con los mismos números ordenados de menor a mayor. Por ejemplo, si recibe [5, 10, 7, 3] debe devolver [3, 5, 7, 10].

# Primera parte

def verificar_paridad(lista):
    largo = len(lista)
    if (largo % 2) == 0:
        return True
    else:
        return False
    
# Segunda parte

def encontrar_extremos(lista):
    maximo = lista[0]
    minimo = lista[0]

    for numero in lista:
        if numero > maximo:
            maximo = numero
        if numero < minimo:
            minimo = numero
    
    return maximo, minimo

# Tercera parte

def ordenar_lista(lista):
    lista_nueva = list(lista)
    lista_nueva.sort()
    return lista_nueva

# Ejemplo de uso

mi_lista = [5, 10, 7, 3]

# Prueba de la primera parte
print("¿La longitud es par?", verificar_paridad(mi_lista))

# Prueba de la segunda parte
max_val, min_val = encontrar_extremos(mi_lista)
print("El maximo es:", max_val)
print("El minimo es:", min_val)

# Prueba de la tercera parte
lista_ordenada = ordenar_lista(mi_lista)
print("Lista ordenada:", lista_ordenada)


# Ejercicio 7 - Modificar tupla / lista por índice o por valor

# EJERCICIO DADO -- Escribir una función que reciba una tupla, un índice, y un nuevo valor. 
# La función debe modificar la tupla, cambiando el valor en la posición dada por el índice, por el nuevo valor pasado como parámetro. 
# Devolver la tupla modificada.

# Repetir el ejercicio anterior, pero con una lista.

# Repetir ambos si ahora, en vez de recibir un índice, se recibe el valor a eliminar. 
# Si no se contiene al valor, se devuelve la estructura tal cual se recibió.

# Primera parte

def modificar_tupla(tupla_orig, indice, valor):
    lista_temp = list(tupla_orig)
    lista_temp[indice] = valor
    return tuple(lista_temp)

# Segunda parte

def modificar_lista(lista_orig, indice, valor):
    lista_orig[indice] = valor
    return lista_orig

# Tercera parte

def eliminar_por_valor(estructura, valor_a_borrar):
    # Verificar si el valor existe para evitar errores
    if valor_a_borrar not in estructura:
        return estructura
        
    if isinstance(estructura, tuple):
        temp = list(estructura)
        temp.remove(valor_a_borrar)
        return tuple(temp)
    
    elif isinstance(estructura, list):
        # Crear una copia para no modificar la original accidentalmente
        nueva_lista = list(estructura)
        nueva_lista.remove(valor_a_borrar)
        return nueva_lista
    
    return estructura

# Ejemplos de uso

t = (1, 2, 3)
l = [10, 20, 30]

print("Tupla modificada:", modificar_tupla(t, 1, 99))
print("Lista modificada:", modificar_lista(l, 0, 100))

# Prueba eliminando valor
print("Eliminar 20 de lista:", eliminar_por_valor(l, 20))
print("Eliminar 3 de tupla:", eliminar_por_valor(t, 3))
print("Intentar eliminar inexistente:", eliminar_por_valor(t, 500))

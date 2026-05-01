# Ejercicio 9 - Lista invertida

# EJERCICIO DADO -- Escribir una función que reciba una lista de números y devuelva la misma lista en orden inverso.

def invertir_lista(lista_orig):
    lista_nueva = []
    indice = len(lista_orig) - 1

    while indice >= 0:
        lista_nueva.append(lista_orig[indice])
        indice = indice - 1

    return lista_nueva

# Ejemplo de uso

original = [10, 20, 30, 40, 50]
invertida = invertir_lista(original)

print("Original:", original)
print("Invertida:", invertida)

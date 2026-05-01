# Ejercicio 6 - Caracteres no vocales como tupla — sin `for` (`filter`)

# EJERCICIO DADO -- Escribir una función que, dada una cadena de caracteres, devuelva una tupla con cada uno de los caracteres que no es una vocal.

# Restricción: no se permite el uso de ciclos for/while


def EsConsonanteOSimbolo(caracter):
    vocales = "aeiouAEIOU"

    if caracter in vocales:
        return False
    else:
        return True
    

def ObtenerNoVocales(texto):
    resultado = tuple(filter(EsConsonanteOSimbolo, texto))
    return resultado

# Ejemplo de uso:

print(f"Algoritmos -> {ObtenerNoVocales('Algoritmos')}")

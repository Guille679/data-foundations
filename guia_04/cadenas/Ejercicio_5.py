# Ejercicio 5 - Caracteres en mayúscula como lista — sin `for` (`map`)

# EJERCICIO DADO --  Escribir una función que, dada una cadena de caracteres, devuelva una lista con cada uno de los caracteres que la componen en mayúscula. 

# Restricción: no se permite el uso de ciclos for/while.


def ConvertirAListaMayusculas(texto):

    resultado = list(map(str.upper, texto))

    return resultado

# Ejemplo de uso:

resultado1 = ConvertirAListaMayusculas("Hola")
print(f"Resultado 1: {resultado1}") 
# Ejercicio 7 - Índice del último carácter — sin `for`

# EJERCICIO DADO -- Escribir una función que, dada una cadena de caracteres, devuelva el número de índice de posición del último caracter.

# Restricción: no se permite el uso de ciclos for/while.


def ObtenerUltimoIndice(texto):
    largo = len(texto)

    if largo == 0:
        return "La cadena esta vacia"
    else:
        return largo - 1
    
# Ejemplo de uso:

print(f"Ultimo indice de 'Hola': {ObtenerUltimoIndice('Hola')}") 
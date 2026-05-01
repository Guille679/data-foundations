# Ejercicio 2 - Separación de miles en un número como string

# EJERCICIO DADO -- Escribir una función que reciba una cadena que contiene un largo número entero y devuelva una cadena con el número y las separaciones de miles.

def FormatearMiles(numero_original):
    
    nueva_cadena = ""
    contador = 0
    largo = len(numero_original)
    
    for i in range(largo - 1, -1, -1):
        
        nueva_cadena = numero_original[i] + nueva_cadena
        contador = contador + 1

        if contador == 3 and i > 0:
            nueva_cadena = "." + nueva_cadena
            contador = 0

    return nueva_cadena

# Ejemplo de uso:

entrada = input("Escribe un numero largo: ")
resultado = FormatearMiles(entrada)
print("Numero formateado:", resultado)

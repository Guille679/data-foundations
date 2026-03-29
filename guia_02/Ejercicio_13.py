# Ejercicio 13 - Función: cantidad de letras de una palabra

# EJERCICIO DADO -- Hacer una función que reciba una palabra y devuelva la cantidad de letras que tiene.

def contar_letras(palabra):
    
    # Se utiliza len() porque devuelve la longitud de la cadena dada
    cantidad = len(palabra)
    return cantidad

# Ejemplo de uso

resultado = contar_letras("Python")
print(f"La palabra tiene {resultado} letras.")

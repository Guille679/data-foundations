# Ejercicio 5 - Palabra más larga por carácter

# EJERCICIO DADO -- Escribir una función que reciba un texto y para cada caracter presente en el texto, devuelva la palabra más larga en la que se encuentra ese caracter.

def EncontrarMasLargas(texto):
    # Convertir todo a minusculas para que coincidan letras y palabras
    texto = texto.lower()
    lista_palabras = texto.split()
    resultado = {}

    for caracter in texto:
        # Filtrar espacios y evitar repetir caracteres ya procesados
        if caracter != " " and caracter not in resultado:
            palabra_ganadora = ""

            for palabra in lista_palabras:
                if caracter in palabra:
                    # Comparar longitudes para quedarnos con la mayor
                    if len(palabra) > len(palabra_ganadora):
                        palabra_ganadora = palabra

            resultado[caracter] = palabra_ganadora

    return resultado

# Ejemplo de uso
T = "El hipopotamo corre por el campo"
resultado_final = EncontrarMasLargas(T)

print(resultado_final)

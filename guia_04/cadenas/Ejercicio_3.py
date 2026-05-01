# Ejercicio 3 - Iniciales de una frase, palíndromo

# EJERCICIO DADO -- Escribir funciones que dada una cadena de caracteres:

# Devuelva la primera letra de cada palabra.
# Indique si se trata de un palíndromo.


def ObtenerSiglas(texto):
    
    resultado = ""

    if len(texto) > 0:
        resultado = resultado + texto[0]

    for i in range(len(texto) - 2):
        if texto[i] == " " and texto[ i + 1] != " ":
            resultado = resultado + texto[i + 1]
    
    return resultado



def EsPalindromo(texto):

    texto_limpio = "".join(caracter.lower() for caracter in texto if caracter != " ")

    texto_invertido = texto_limpio[::-1]

    return texto_limpio == texto_invertido


# Ejemplo de uso:

print(ObtenerSiglas("Ciclo Básico Común")) # CBC
print(EsPalindromo("Anita lava la tina"))   # True
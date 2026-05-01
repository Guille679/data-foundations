# Ejercicio 2 - Frecuencia de palabras y caracteres en un string

# EJERCICIO DADO -- Ecriba una función que reciba una cadena y devuelva:

# Un diccionario con la cantidad de apariciones de cada palabra en la cadena. 
# Un diccionario con la cantidad de apariciones de cada caracter en la cadena.

def ContarFrecuencias(texto):
    texto = texto.lower()
    
    diccionario_palabras = {}
    lista_palabras = texto.split()

    for palabra in lista_palabras:
        if palabra in diccionario_palabras:
            diccionario_palabras[palabra] += 1
        else:
            diccionario_palabras[palabra] = 1

    diccionario_caracteres = {}

    for letra in texto:
        if letra != " ":
            if letra in diccionario_caracteres:
                diccionario_caracteres[letra] += 1
            else:
                diccionario_caracteres[letra] = 1
    
    return diccionario_palabras, diccionario_caracteres

# Ejemplo de uso

cadena = "Que lindo esta el dia"
res_palabra, res_caracter = ContarFrecuencias(cadena)

print(f"Conteo de palabras: {res_palabra}")
print(f"Conteo de caracteres: {res_caracter}")

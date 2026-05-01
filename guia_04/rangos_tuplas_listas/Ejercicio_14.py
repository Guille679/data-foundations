# Ejercicio 14 - Ordenar palabras y unirlas en string

# EJERCICIO DADO -- Hacer una función que reciba una lista de palabras, las ordene en orden alfabético y luego las una en un string separadas por espacios.

def ordenar_y_unir(lista_palabras):
    lista_ordenada = sorted(lista_palabras)
    texto_final = " ".join(lista_ordenada)

    return texto_final


# Ejemplo de uso

entrada = ["manzana", "perro", "casa", "arbol"]
resultado = ordenar_y_unir(entrada)

print(f"Lista original: {entrada}")
print(f"Resultado: '{resultado}'")
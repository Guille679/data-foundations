# Ejercicio 1 - Convertir lista de tuplas a diccionario

# EJERCICIO DADO -- Escribir una función que reciba una lista de tuplas, y que devuelva un diccionario en donde las claves sean los primeros elementos de las tuplas, y los valores una lista con los segundos.

def AgruparElementos(lista_de_tuplas):
    diccionario_resultado = {}

    for tupla in lista_de_tuplas:
        clave = tupla[0]
        valor = tupla[1]

        if clave not in diccionario_resultado:
            diccionario_resultado[clave] = [valor]
        else:
            diccionario_resultado[clave].append(valor)
        
    return diccionario_resultado

# Ejemplo de uso

entrada = [("fruta", "manzana"), ("verdura", "apio"), ("fruta", "pera")]
resultado = AgruparElementos(entrada)

print(f"Diccionario agregado: {resultado}")


# Ejercicio EC - Evaluación de código: identificar y corregir errores

# EJERCICIO DADO -- En estos ejercicios se presenta código con errores, malas prácticas de programación o problemas de eficiencia. 
# El objetivo es identificar los errores, explicar por qué fallan y proponer una corrección.

# Ejercicio 1
# El siguiente código intenta obtener el último elemento de una lista, pero contiene errores. Identificá por qué falla y corregilo.

def obtener_ultimo():
    ultimo = lista[len(lista)]
    return ultimo

# --- Ejercicio 1 corregido ---

def obtener_ultimo(lista):
    if not lista:
        return None
    return lista[len(lista) - 1]

# Ejemplo de uso
mi_lista = [1, 2, 3, 4, 5]
print(obtener_ultimo(mi_lista))


# ------------------------------------------------------------------------------------------------------------------------------------------


# Ejercicio 2
# El siguiente código intenta modificar una tupla, pero contiene errores. Explicá qué ocurre y proponé una solución alternativa.

def cambiar_segundo_elemento(tupla, nuevo_valor):
    tupla[1] = nuevo_valor
    return tupla

# -- Ejercicio 2 corregido --

def cambiar_segundo_elemento(tupla, nuevo_valor):
    lista_temporal = list(tupla)
    if len(lista_temporal) > 1:
        lista_temporal[1] = nuevo_valor
    return tuple(lista_temporal)

# Ejemplo de uso
mi_tupla = (10, 20, 30)
print(cambiar_segundo_elemento(mi_tupla, 99))

# ------------------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 3
contador = {
    'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
}

def contar_letras(palabra):
    for letra in palabra:
        contador[letra] = contador[letra] + 1
    return contador

# -- Ejercicio 3 corregido --

def contar_letras(palabra):
    contador = {}
    for letra in palabra:
        if letra in contador:
            contador[letra] += 1
        else:
            contador[letra] = 1
    return contador

# Ejemplo de uso
print(contar_letras("algoritmos"))


# ------------------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 4
# En una biblioteca se tiene un catálogo de libros donde cada código de libro es una clave de un diccionario. Los valores son diccionarios con la información del libro: título, autor y si está disponible para préstamo o no.
# El siguiente código intenta eliminar del catálogo todos los libros que no están disponibles y devolver en una tupla los libros eliminados. Identificá los errores y corregilo.

# Ejemplo de catálogo de libros
catalogo = {
    "LIB001": {"titulo": "Cien años de soledad", "autor": "García Márquez", "disponible": True},
    "LIB002": {"titulo": "El túnel", "autor": "Ernesto Sabato", "disponible": False},
    "LIB003": {"titulo": "Rayuela", "autor": "Julio Cortázar", "disponible": True},
    "LIB004": {"titulo": "Ficciones", "autor": "Jorge Luis Borges", "disponible": False},
}

def eliminar_no_disponibles_devolver_eliminados_de_diccionario(libros):
    eliminados = {}
    for codigo in libros:
        if libros[codigo]["disponible"] == False and libros[codigo]["disponible"] != True:
            eliminados.append(libros[codigo])
            del libros[codigo]
    return eliminados.filter( { libros[codigo]["disponible"] != True })

# -- Ejercicio 4 corregido --
def eliminar_no_disponibles(libros):
    eliminados = {}
    codigos_a_borrar = []
    
    for codigo, info in libros.items():
        if info["disponible"] == False:
            eliminados[codigo] = info
            codigos_a_borrar.append(codigo)
            
    for codigo in codigos_a_borrar:
        del libros[codigo]
        
    return (eliminados,)

# Ejemplo de uso
catalogo = {
    "LIB001": {"titulo": "Cien años de soledad", "autor": "García Márquez", "disponible": True},
    "LIB002": {"titulo": "El túnel", "autor": "Ernesto Sabato", "disponible": False},
    "LIB003": {"titulo": "Rayuela", "autor": "Julio Cortázar", "disponible": True},
    "LIB004": {"titulo": "Ficciones", "autor": "Jorge Luis Borges", "disponible": False},
}

resultado = eliminar_no_disponibles(catalogo)
print(resultado)


# ------------------------------------------------------------------------------------------------------------------------------------------
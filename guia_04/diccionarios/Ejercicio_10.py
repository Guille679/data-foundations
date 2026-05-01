# Ejercicio 10 - Películas con puntaje > 7 (con y sin `filter`)

# EJERCICIO DADO -- Rosita tiene una lista de diccionarios donde guarda todas las películas que vió. 
# La información para cada una es: el nombre de la película, año en que salió, y la puntuación que le puso del 1 al 10. 
# Hacer una función que reciba el diccionario y devuelva una nueva lista de diccionarios donde sólo estén las películas que tienen puntaje mayor a 7.

# Resolver sin usar filter
# Resolver usando filter.

def peliculas_buenas_bucle(lista_peliculas):
    filtradas = []
    for pelicula in lista_peliculas:
        if pelicula["puntuacion"] > 7:
            filtradas.append(pelicula)
    return filtradas

# Ejemplo de uso 
vistas = [
    {"nombre": "Toy Story", "año": 1995, "puntuacion": 10},
    {"nombre": "Sharknado", "año": 2013, "puntuacion": 3},
    {"nombre": "Batman", "año": 2022, "puntuacion": 8}
]

print("Sin filter:", peliculas_buenas_bucle(vistas))


def peliculas_buenas_filter(lista_peliculas):
    # La lambda toma cada pelicula y chequea si su puntaje es > 7
    resultado = filter(lambda p: p["puntuacion"] > 7, lista_peliculas)
    
    # filter devuelve un objeto especial, por lo que hay que convertirlo a lista
    return list(resultado)

# Ejemplo de uso
print("Con filter:", peliculas_buenas_filter(vistas))

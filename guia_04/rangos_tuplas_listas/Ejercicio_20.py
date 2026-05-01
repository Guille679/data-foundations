# Ejercicio 20 - Contar libros repetidos con diccionario

# EJERCICIO DADO -- Se tiene una base de datos con nombres de libros de la siguiente forma ["La Noche de la Usina", "La Pregunta de sus Ojos", "Ser Feliz era Esto",...], y se quiere saber cuántos libros repetidos tienen. Escribir una función que reciba la base de datos y devuelva, para cada uno de los títulos, cuántos ejemplares hay. La lista no tiene un tamaño fijo, y puede contener muchos títulos repetidos.

def contar_ejemplares(lista_libros):
    conteo = {}
    
    for titulo in lista_libros:
        if titulo in conteo:
            # Si ya existe, sumar 1 al valor actual
            conteo[titulo] += 1
        else:
            # Si es la primera vez que lo vemos, lo iniciamos en 1
            conteo[titulo] = 1
            
    return conteo

# Ejemplo de uso
base_de_datos = [
    "La Noche de la Usina", 
    "La Pregunta de sus Ojos", 
    "Ser Feliz era Esto",
    "La Noche de la Usina",
    "La Noche de la Usina",
    "Ser Feliz era Esto"
]

resultado = contar_ejemplares(base_de_datos)

print("Reporte de ejemplares:")
for titulo, cantidad in resultado.items():
    print(f"Libro: {titulo} - Cantidad: {cantidad}")

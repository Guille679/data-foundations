# Ejercicio 8 - Valores de una clave en lista de diccionarios

# EJERCICIO DADO -- Escribir una función que reciba una lista de diccionarios y una clave, y devuelva una lista con los valores correspondientes a esa clave.

def obtener_valores_por_clave(lista_diccionarios, clave_buscada):
    valores = []
    
    for diccionario in lista_diccionarios:
        if clave_buscada in diccionario:
            valores.append(diccionario[clave_buscada])
            
    return valores

# Ejemplo de uso
estudiantes = [
    {"nombre": "Violeta", "carrera": "Informatica"},
    {"nombre": "Carla", "carrera": "Mecanica"},
    {"nombre": "Manuela", "carrera": "Quimica"}
]

solo_nombres = obtener_valores_por_clave(estudiantes, "nombre")
print(f"Lista de nombres: {solo_nombres}")

solo_carreras = obtener_valores_por_clave(estudiantes, "carrera")
print(f"Lista de carreras: {solo_carreras}")

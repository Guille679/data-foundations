# Ejercicio 12 - Eliminar productos sin control de calidad

# EJERCICIO DADO -- En una fábrica se tiene una base de datos donde se guardan todos los códigos de los productos que se fabrican como claves de un diccionario. 
# Los valores de cada clave son nuevos diccionarios, con la siguiente información: fecha de vencimiento (mes,año), si pasó el chequeo de calidad o no.

# Se pide hacer una función que reciba esta lista de diccionarios, y elimine a todos los productos que no pasaron el chequeo de calidad. 
# Devolver en una tuple todos los productos eliminados en formato {codigo: diccionario del producto}.

def limpiar_productos_fallidos(db_productos):
    eliminados = {}
    codigos_a_borrar = []

    # 1. Identificar cuales no pasaron el chequeo
    for codigo, info in db_productos.items():
        if not info["calidad"]: # Si paso_calidad es False
            eliminados[codigo] = info
            codigos_a_borrar.append(codigo)
    
    # 2. Eliminarlos del diccionario original
    for codigo in codigos_a_borrar:
        del db_productos[codigo]
        
    # 3. Devolver los eliminados como una tupla
    return (eliminados,)

# Ejemplo de uso
productos = {
    "PROD01": {"vencimiento": (10, 2025), "calidad": True},
    "PROD02": {"vencimiento": (5, 2024), "calidad": False},
    "PROD03": {"vencimiento": (12, 2026), "calidad": False},
    "PROD04": {"vencimiento": (1, 2025), "calidad": True}
}

productos_borrados = limpiar_productos_fallidos(productos)

print("Productos que quedaron en la base:", productos)
print("Tupla de productos eliminados:", productos_borrados)

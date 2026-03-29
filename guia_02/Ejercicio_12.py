# Ejercicio 12 - Función: imprimir nombre en formato "Apellido, Nombre"

# EJERCICIO DADO -- Crear una función que le pida al usuario su nombre y apellido, e los imprima con el siguiente formato: “Apellido, Nombre”.


def formatear_nombre():
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    
    # Se utiliza f-string para el formato "Apellido, Nombre"
    return f"{apellido}, {nombre}"
    

# Ejemplo de uso

uso = formatear_nombre()
print(uso)
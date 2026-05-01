# Ejercicio 3 -  Función: cantar el feliz cumpleaños N veces 

# EJERCICIO DADO -- Crear una función que cante el feliz cumpleaños. 
# Dado un entero, debe imprimir ‘Que los cumplas feliz’ en distintas líneas por esa cantidad de veces.

def cantar_cumple(cantidad):
    for i in range(1, cantidad + 1):
        print ("Que los cumplas feliz")


# Ejemplo de uso
veces = int(input("¿Cuantas veces queres cantar? "))
resultado = cantar_cumple(veces)


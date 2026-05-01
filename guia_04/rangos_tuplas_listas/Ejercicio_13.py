# Ejercicio 13 - Lista de supermercado con `input`

# EJERCICIO DADO -- Se quiere crear una lista de supermercado, solicitándole al usuario productos hasta que ingrese el valor ‘X’. 
# La función debe devolver los productos en un string, separados por comas.

def crear_lista_super():
    lista_temporal = []
    entrada = ""

    # Usamos .upper() para que acepte tanto 'X' como 'x'
    while entrada.upper() != "X":
        entrada = input("Ingrese producto o X para terminar: ")

        if entrada.upper() != "X":
            lista_temporal.append(entrada)
    
    resultado_texto = ", ".join(lista_temporal)
    return resultado_texto

# Ejemplo de uso
mi_compra = crear_lista_super()
print("Tu lista de compras es:", mi_compra)

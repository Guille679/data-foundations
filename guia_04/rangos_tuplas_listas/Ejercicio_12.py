# Ejercicio 12 - Lista de supermercado desde string CSV 

# EJERCICIO DADO -- Se tiene una lista de supermercado escrita como string con productos separados por coma: "pan, arroz, pescado, jugo, fideos,...".

# Escribir una función que reciba la cadena de caracteres de los productos de supermercado y devuelva una lista con cada uno de los productos por separado: ['pan', 'arroz', 'pescado', 'jugo', 'fideos', ...].

# Se tiene además otra cadena de caracteres con los precios de cada producto: "100, 50, 200, 80, 30,...". Escribir una función que reciba ambas cadenas y devuelva una lista con tuplas de (producto, precio): [('pan', 100), ('arroz', 50), ('pescado', 200), ('jugo', 80), ('fideos', 30), ...].

# Para la función del punto anterior, escribir otra función que reciba la lista de tuplas y devuelva el precio total de la lista de compras.

# Primera parte

def separar_productos(cadena):
    lista_limpia = [item.strip() for item in cadena.split(',')]
    return lista_limpia

# Segunda parte

def combinar_datos(cadena_prod, cadena_precios):
    lista_p = cadena_prod.split(",")
    lista_v = cadena_precios.split(",")
    
    resultado = []

    # Usar min para evitar errores de indice si las listas no coinciden
    for i in range(min(len(lista_p), len(lista_v))):
        tupla = (lista_p[i].strip(), lista_v[i].strip())
        resultado.append(tupla)
        
    return resultado

# Tercera parte

def calcular_total(lista_tuplas):
    total = 0
    for producto, precio in lista_tuplas:
        # Convertir a entero para poder sumar
        total = total + int(precio)
    return total

# Ejemplo de uso

productos_str = "pan, arroz, pescado, jugo, fideos"
precios_str = "100, 50, 200, 80, 30"

# 1. Separar
lista_prod = separar_productos(productos_str)
print("Lista de productos:", lista_prod)

# 2. Combinar
lista_combinada = combinar_datos(productos_str, precios_str)
print("Productos con precios:", lista_combinada)

# 3. Total
total_compra = calcular_total(lista_combinada)
print("El precio total es:", total_compra)


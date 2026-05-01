# Ejercicio 18 - Desafío: sistema de facturación

# EJERCICIO DADO -- Desafio (no obligatorio): Sistema de facturación simplificado.

# Se cuenta con una lista ordenada de productos con tuplas de (identificador, descripción, precio), y una lista de los productos a facturar, con tuplas de (identificador, cantidad).

# Se desea generar una factura que incluya la cantidad, la descripción, el precio unitario y el precio total de cada prod_comprado, y al final imprima el total general.

# Escribir una función que reciba ambas listas e imprima por pantalla la factura solicitada.

def generar_factura(lista_productos, lista_compras):
    total_general = 0
    print("\n--- FACTURA DE VENTA ---")
    print("Cant | Descripcion | Unitario | Subtotal")
    
    for id_compra, cantidad in lista_compras:
        # Buscar el producto en la lista maestra
        for id_prod, descripcion, precio in lista_productos:
            if id_compra == id_prod:
                subtotal = precio * cantidad
                total_general += subtotal
                
                # Imprimir la linea de la factura
                print(f"{cantidad} x {descripcion} | ${precio} | ${subtotal}")
    
    print("-" * 30)
    print(f"TOTAL GENERAL: ${total_general}")

# Ejemplo de uso

# Prueba Facturacion
stock = [(1, "Pan", 100), (2, "Leche", 150), (3, "Jugo", 80)]
compras = [(1, 2), (3, 5)] # 2 panes (id 1) y 5 jugos (id 3)

generar_factura(stock, compras)

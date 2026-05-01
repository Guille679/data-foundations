# Ejercicio 4 -  Función: cobro en supermercado (sin y con vuelto)

# EJERCICIO DADO -- Necesitamos escribir un programa de cobro en el supermercado. 
# La función debe recibir un número entero que representa el monto a pagar y debe permitir al usuario que ingrese valores, 
# hasta que el pago se haya realizado en su totalidad. 
# Además, le debe ir indicando cuánto le queda por pagar. El programa no da vuelto.

# Ejemplo:

# Su total a pagar es: 500
# Ingrese el monto a pagar: 100
# Pendientes: 400. Ingrese el monto a pagar: 200
# Pendientes: 200. Ingrese el monto a pagar: 200
# Pendientes: 0. Gracias por su compra.


# Sin vuelto
def cobrar_supermercado(monto_total):
    pendiente = monto_total
    print(f"Su total a pagar es: {pendiente}")

    while pendiente > 0:

        # Pedir el pago y convertirlo a entero
        pago = int(input(f"Pendientes: {pendiente}. Ingrese el monto a pagar: "))
        
        # Restar lo que pago al total pendiente
        pendiente = pendiente - pago

    print("Pendientes: 0. Gracias por su compra.")

# Ejemplo de uso:
cobrar_supermercado(500)

print ("---" * 30)

# Con vuelto 
def cobrar_con_vuelto(monto_total):
    pendiente = monto_total
    vuelto = 0
    print(f"Su total a pagar es: {pendiente}")

    while pendiente > 0:
        pago = int(input(f"Pendientes: {pendiente}. Ingrese el monto a pagar: "))
        pendiente -= pago

    # Si el pendiente es negativo, se calcula el vuelto
    if pendiente < 0:
        vuelto = abs(pendiente) # abs() para convertir el numero a positivo
    
    print(f"Pendientes: 0. Su vuelto es: {vuelto}. Gracias por su compra.")

# Ejemplo de uso
cobrar_con_vuelto(500)

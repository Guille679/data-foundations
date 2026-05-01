# Ejercicio 9 - Ticket de supermercado: monto total

# EJERCICIO DADO -- Se tiene un ticket de supermercado en forma de diccionario con los siguientes datos:

# Nombre del Producto
# Precio por Unidad
# Cantidad

# Se pide hacer una función que reciba el ticket y devuelva el monto a pagar total.

def calcular_total_ticket(ticket):
    total = 0
    
    for producto in ticket:
        # Extraer los datos del diccionario
        precio = ticket[producto]["precio_unidad"]
        cantidad = ticket[producto]["cantidad"]
        
        # Sumar el subtotal al acumulador
        total += precio * cantidad
        
    return total

# Ejemplo de uso 
# Estructura del ticket: { "Producto": {"precio_unidad": X, "cantidad": Y} }

mi_ticket = {
    "Leche": {"precio_unidad": 1200, "cantidad": 2},
    "Pan": {"precio_unidad": 1500, "cantidad": 1},
    "Yerba": {"precio_unidad": 3500, "cantidad": 3}
}

monto_final = calcular_total_ticket(mi_ticket)
print(f"El total a pagar es: ${monto_final}")

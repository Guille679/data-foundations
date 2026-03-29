# Ejercicio 3 - Operaciones aritméticas entre variables.

# EJERCICIO DADO -- Guardar los números 1, 2 y 3 en tres variables distintas
# y luego sumarlos e imprimir el resultado por pantalla. Repetir con las
# distintas operaciones: resta, multiplicación, división, división entera,
# resto, potencia; combinando los números entre sí.

# Definición de variables
a = 1
b = 2
c = 3

# Operaciones
suma = a + b + c
resta = c - b - a
multiplicacion = a * b * c
division = c / b
division_entera = c // b
resto = c % b
potencia = b ** c

# Impresión de resultados
print(f"Suma (1+2+3): {suma}")
print(f"Resta (3-2-1): {resta}")
print(f"Multiplicación (1*2*3): {multiplicacion}")
print(f"División (3/2): {division}")
print(f"División entera (3//2): {division_entera}")
print(f"Resto (3%2): {resto}")
print(f"Potencia (2^3): {potencia}")

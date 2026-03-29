# Ejercicio 6 - Calcular edad a partir del año de nacimiento

# EJERCICIO DADO -- Escribir un programa que le pida al usuario su año de nacimiento, y que le diga qué edad tiene en el año actual.

# Solicitud de año de nacimiento
anio_nacimiento = int(input("Ingresa tu año de nacimiento: "))

# Año actual
anio_actual = 2026

# Cálculo de la edad
edad = anio_actual - anio_nacimiento

# Impresión del resultado
print(f"Tenés (o vas a cumplir) {edad} años en este {anio_actual}.")

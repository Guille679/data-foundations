# Ejercicio 17 - Función: conversión Celsius ↔ Fahrenheit

# EJERCICIO DADO -- Escribir una función que convierta un valor dado en grado Celsius, a Fahrenheit. 
# recordar que la fórmula para la conversión es: F = 9/5 * C + 32.
# Escribir una función que convierta un valor dado en grados Fahrenheit, a Celsius. Usar la misma fórmula anterior.

def celsius_a_fahrenheit(c):
    f = (9 / 5) * c + 32
    return f

# Ejemplo: 0°C debería ser 32°F
print(celsius_a_fahrenheit(0)) 


def fahrenheit_a_celsius(f):
    # Los paréntesis son importantes para que la resta se haga primero
    c = (f - 32) * 5 / 9
    return c

# Ejemplo: 212°F (punto de ebullición) debería ser 100°C
print(fahrenheit_a_celsius(212))



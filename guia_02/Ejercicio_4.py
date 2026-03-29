# Ejercicio 4 - Programa con `input`: nombre y edad

# EJERCICIO DADO -- Crear un programa que le solicite al usuario:
# Su nombre y lo imprima por pantalla.
# Su edad y la imprima por pantalla.
# Su edad, le sume 1, y la imprima por pantalla.

# Solicitud de nombre
nombre = input("Ingresa tu nombre: ")
print(f"Tu nombre es: {nombre}")

# Solicitud de edad
# Usamos int() para que el dato sea un número y no texto
edad = int(input("Ingresa tu edad: "))
print(f"Tu edad es: {edad}")

# Sumar 1 a la edad e imprimir
edad_proximo_anio = edad + 1
print(f"El próximo año tendrás: {edad_proximo_anio}")

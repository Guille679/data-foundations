# Ejercicio 7 - Promedio de 5 enteros (dos versiones)

# EJERCICIO DADO -- Crear un programa que le solicite al usuario 5 enteros y que muestre por pantalla el promedio de ellos. Hacerlo de dos formas:
# Primero, usando 5 variables para cada entero.
# Después, usando una sola variable para almacenar la suma de los 5 enteros. ¿Cómo se te ocurre que podrías hacer?

# Primer version

# Solicitud de los 5 números en variables distintas
n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
n3 = int(input("Ingrese el tercer número: "))
n4 = int(input("Ingrese el cuarto número: "))
n5 = int(input("Ingrese el quinto número: "))

# Cálculo del promedio
promedio = (n1 + n2 + n3 + n4 + n5) / 5

print(f"El promedio con 5 variables es: {promedio}")


# Segunda version
 
# Inicializamos una variable en 0 para acumular la suma
suma_total = 0

# Vamos sumando cada input directamente a la variable
suma_total += int(input("Ingrese el primer número: "))
suma_total += int(input("Ingrese el segundo número: "))
suma_total += int(input("Ingrese el tercer número: "))
suma_total += int(input("Ingrese el cuarto número: "))
suma_total += int(input("Ingrese el quinto número: "))

# Cálculo del promedio final
promedio_optimizado = suma_total / 5

print(f"El promedio con una sola variable acumuladora es: {promedio_optimizado}")

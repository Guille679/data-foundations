# Ejercicio 9 - Función: detectar si un número es par

# EJERCICIO DADO -- Crear una función que reciba un número y que devuelva True si es par, y False si es impar.

def es_par(numero):
    return numero % 2 == 0

# Ejemplo de uso 1: Guardando el resultado en una sola variable
resultado = es_par(10)
print(f"¿Es 10 un número par?: {resultado}")

# Ejemplo de uso 2: Usando un input del usuario
num_usuario = int(input("Ingresa un número para saber si es par: "))
if es_par(num_usuario):
    print("¡Es par!")
else:
    print("Es impar.")
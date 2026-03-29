# Ejercicio 18 - Función: área de un triángulo

# EJERCICIO DADO -- Escribir una función que calcule el área de un triángulo recibiendo como parámetros su base y su altura.

def calcular_area_triangulo(base, altura):
    # Usar paréntesis para asegurar el orden de la operación
    area = (base * altura) / 2
    return area

# Ejemplo de uso:

# Un triángulo de base 10 y altura 5
resultado = calcular_area_triangulo(10, 5)
print(f"El área del triángulo es: {resultado}")


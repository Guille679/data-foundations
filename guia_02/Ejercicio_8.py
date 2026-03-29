# Ejercicio 8 - Función: valor absoluto propio

# EJERCICIO DADO -- Crear una función que reciba un número y que devuelva el valor absoluto.

# ¡IMPORTANTE! --> A partir de ahora y en adelante, todo lo que se nos pida (incluso si dice “programa”) se debe realizar dentro de una o más funciones.

def obtener_valor_absoluto(numero):
    if numero < 0:
        return numero * -1
    return numero

# Ejemplo de uso:
num = int(input("Ingresa un número: "))
resultado = obtener_valor_absoluto(num)
print(f"El valor absoluto de {num} es: {resultado}")

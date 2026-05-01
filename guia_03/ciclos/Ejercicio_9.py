# Ejercicio 9 -  Función: detectar si un número es primo

# EJERCICIO DADO -- Crear una función que calcule si un número es primo o no. 
# Un número es primo cuando solamente es divisible por sí mismo y por 1.

def es_primo(numero):
    # Los números menores a 2 (0, 1, negativos) no son primos
    if numero < 2:
        return False
    
    # Probar dividir el número por todos los anteriores (desde 2)
    for i in range(2, numero):
        if numero % i == 0:
            # Si el resto es 0, encontramos un divisor, no es primo
            return False
            
    # Si salió del bucle sin encontrar divisores, es primo
    return True

# Pruebas:
num = int(input("Ingrese un numero para saber si es primo: "))

if es_primo(num):
    print(f"El {num} es primo.")
else:
    print(f"El {num} NO es primo.")

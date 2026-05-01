# Ejercicio 1 - Funciones con `for`: imprimir rangos, saludos, suma, pares, par/impar

# EJERCICIO DADO -- Escribir función que:

# Imprima por pantalla todos los números entre 10 y 20.
# Salude a todas las personas de esta lista [Flaminia, Serena, Agustina, Priscila, Sol, Agostina, Iara, Lu] con el mensaje "Hola <nombre>! Vamos a aprender a programar".
# Le pida al usuario que ingrese 5 números y le muestre la suma total de todos ellos.
# Imprima por pantalla todos los números entre 100 y 199 que sean divisibles por 7.
# Reciba dos números, y recorra todos los números entre ellos, imprimiendo en pantalla si es par o impar.

def ejercicios_combinados(inicio, fin):
    # 1) Números entre 10 y 20
    print("--- Números del 10 al 20 ---")
    for i in range(10, 21): 
        print(i)
    
    # 2) Saludos a la lista
    print("\n--- Saludos ---")
    lista_nombres = ["Flaminia", "Serena", "Agustina", "Priscila", "Sol", "Agostina", "Iara", "Lu"]
    for nombre in lista_nombres:
        print(f"Hola {nombre}! Vamos a aprender a programar") 
    
    # 3) Pedir 5 números y sumarlos
    print("\n--- Suma de 5 números ---")
    suma_total = 0
    for i in range(5):
        num = int(input(f"Ingrese el número {i+1}: "))
        suma_total += num 
    print(f"La suma total es: {suma_total}")

    # 4) Divisibles por 7 entre 100 y 199
    print("\n--- Divisibles por 7 entre 100 y 199 ---")
    for i in range(100, 200): # 200 para incluir el 199
        if i % 7 == 0:
            print(i)

    # 5) Recorrer rango y decir si es par o impar
    print(f"\n--- Par o Impar entre {inicio} y {fin} ---")
    for i in range(inicio, fin + 1): # fin + 1 para incluir el último número
        if i % 2 == 0:
            print(f"{i} es par")
        else:
            print(f"{i} es impar")


# Ejemplo de uso:

test = ejercicios_combinados(1, 3)
print(test)

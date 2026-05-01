# Ejercicio 11 - ⭐ Desafío: suma/promedio de múltiplos de 7 en un rango

# EJERCICIO DADO -- Desafío (obligatorio):
# Crear una función que reciba dos números, y devuelva la suma de todos los números múltiplos de 7 entre esos dos números. 
# Por ejemplo, si recibe 3 y 25, debe devolver 7 + 14 + 21 = 42. 
# Si recibe 3 y 4, debe devolver 0, ya que no hay múltiplos de 7 entre esos dos números.

# Repetir calculando el promedio en vez de la suma.
# Repetir calculando únicamente el promedio entre los primeros 3 múltiplos de 7 encontrados.
# Repetir calculando únicamente el promedio entre los múltiplos de 7 encontrados que no sean múltiplos de 2.


# Suma de multiplos de 7

def suma_multiplos_7(inicio, fin):
    suma = 0
    # Usar +1 para incluir el numero de fin en la búsqueda
    for i in range(inicio, fin + 1):
        if i % 7 == 0:
            suma += i
    return suma


# Promedio de multiplos de 7

def promedio_multiplos_7(inicio, fin):
    suma = 0
    cantidad = 0
    for i in range(inicio, fin + 1):
        if i % 7 == 0:
            suma += i
            cantidad += 1
    
    if cantidad == 0:
        return 0
    return suma / cantidad


# Promedio de los primeros 3 encontrados

def promedio_primeros_tres(inicio, fin):
    suma = 0
    cantidad = 0
    for i in range(inicio, fin + 1):
        if i % 7 == 0:
            suma += i
            cantidad += 1
            # Si ya se encontro los 3, dejar de buscar
            if cantidad == 3:
                break
    
    if cantidad == 0:
        return 0
    return suma / cantidad

# Ejemplos de uso

# --- Prueba 1: Suma de todos los múltiplos de 7 ---
print("Suma de multiplos de 7 entre 3 y 25:")
print(suma_multiplos_7(3, 25))  # Debería dar 42 (7 + 14 + 21)


# --- Prueba 2: Promedio de todos los múltiplos de 7 ---
print("\nPromedio de multiplos de 7 entre 1 y 50:")
# Múltiplos: 7, 14, 21, 28, 35, 42, 49 (Suma 196 / 7 números)
print(promedio_multiplos_7(1, 50))  # Debería dar 28.0


# --- Prueba 3: Promedio de los PRIMEROS 3 encontrados ---
print("\nPromedio de los primeros 3 múltiplos de 7 entre 10 y 100:")
# Los primeros tres son: 14, 21, 28. (14 + 21 + 28 = 63. 63 / 3 = 21)
print(promedio_primeros_tres(10, 100))  # Debería dar 21.0



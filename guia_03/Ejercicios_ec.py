# Ejercicio EC - Evaluación de código: identificar y corregir errores

# EJERCICIO DADO -- En estos ejercicios se presenta código con errores, malas prácticas de programación o problemas de eficiencia. 
# El objetivo es identificar los errores, explicar por qué fallan y proponer una corrección.


# Ejercicio 1
# El siguiente código intenta verificar si un número está entre 1 y 10 (inclusive), pero no funciona correctamente para todos los casos y tiene varios problemas. 

def esta_en_rango_entre_numero_1_y_10_con_extremos_inclusive(numero):
    if numero > 1:
        if numero < 10:
            return True
        else:
            return False
    else:
        return False

# Pruebas:
print(esta_en_rango(1))   # Debería dar True
print(esta_en_rango(5))   # Debería dar True
print(esta_en_rango(10))  # Debería dar True

# Error: --> Este codigo presenta dos errores:

# 1) No incluye los extremos: Tal como está escrito (> y <), si se ingresa el 1 o el 10, va a devolver False porque esta buscando que sea estrictamente mayor a 1 y menor a 10.
# 2) Nombre de la funcion: En la definicion se la llama "esta_en_rango_entre_numero_1_y_10_con_extremos_inclusive" pero al momento de probarla se la llama con el nombre "esta_en_rango", por lo cual python no la encontraria.

# --- Ejercicio 1 corregido ---

def esta_en_rango(numero):
    if 1 <= numero <= 10:
        return True
    else:
        return False
    
# Pruebas:
print(esta_en_rango(1))   # Ahora da True
print(esta_en_rango(5))   # Ahora da True
print(esta_en_rango(10))  # Ahora da True


# ------------------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 2
# El siguiente código intenta sumar los números del 1 al N usando un ciclo while, pero ocurre un error.

def suma_hasta(n):
    suma = 0
    i = 1
    while i <= n:
        suma = suma + i
    return suma

# Error --> Este codigo tiene un bucle infinito

# Explicacion: El valor de i siempre es 1. Como nunca cambia, la condición i <= n siempre sera verdadera (si n es 1 o mas), la computadora se quedara sumando por siempre y el programa colapsaria.

# --- Ejercicio 2 corregido ---

def suma_hasta(n):
    suma = 0
    i = 1
    while i <= n:
        suma = suma + i
        i = i + 1  # <--- Faltaba esto para que el bucle avance
    return suma

# Prueba:
print(suma_hasta(5)) # Debería dar 15 (1+2+3+4+5)

# ------------------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 3
# El siguiente código intenta contar cuántos números pares hay en un rango, pero el resultado siempre es incorrecto.

def contar(i, f):
    contador = 0
    for i in range(i, f):
        if i % 2 == 0:
            contador = 1
        return contador
    
# Error --> El codigo presenta 3 errores de logica que hacen que no funcione como deberia:

# 1) El return esta dentro del for: Tal como esta, la funcion hace la primera vuelta del bucle y se corta ahi mismo (devuelve el valor y muere)
# El return siempre tiene que ir afuera del bucle si se quiere que termine de contar todo.

# 2) No esta sumando: El contador = 1 no suma, sino que "pisa" el valor anterior. Para contar se necesita que el contador sea el anterior mas uno.
# 3) El rango no incluye el final: el range(i, f) llega uno antes de f. Si se quiere incluir el numero final se debe usar f + 1

# --- Ejercicio 3 corregido ---

def contar_pares(inicio, fin):
    contador = 0
    # Usar fin + 1 para que incluya el último número
    for i in range(inicio, fin + 1):
        if i % 2 == 0:
            contador = contador + 1
            
    return contador # <--- AFUERA del for para que termine de contar

# Prueba:
print(contar_pares(1, 10)) # Debería dar 5 (2, 4, 6, 8, 10)


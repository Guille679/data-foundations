# Ejercicio EC - Evaluación de código: identificar y corregir errores

# EJERCICIO DADO -- En estos ejercicios se presenta código con errores, malas prácticas de programación o problemas de eficiencia. 
# El objetivo es identificar los errores, explicar por qué fallan y proponer una corrección. 

# Ejercicio 1

# El siguiente código intenta calcular el promedio de tres números, pero tiene varios problemas. Identificá cuál es y corregilo.
def prom(a, b, c):
    suma = a + b + c
    promedio = suma / 3
    
# Error: --> Presenta un error porque para que funcione se debe agregar un return, sin el return, la funcion devuelve por defecto none [1,3]

# --- Ejercicio 1 corregido ---

def prom(a, b, c):
    suma = a + b + c
    promedio = suma / 3
    return promedio

# ------------------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 2

# El siguiente código intenta convertir una temperatura de Celsius a Kelvin, pero tiene varios problemas. Identificá el error y corregilo.
def celsius_a_kelvin(celsius):
    celsius = input("Ingrese la temperatura en Celsius: ")
    kelvin = celsius + 273.15
    print kelvin
    
# Error --> Este codigo presenta dos problemas de jerarquia y diseño:
# 1. Parametro inutil: Se define la funcion con (celsius), pero inmediatamente despues se pide un input que sobrescribe esa variable. El valor que se le envie al llamar la funcion se pierde.
# 2. Falta de return: Al igual que el primer ejemplo, la funcion solo imprime el resultado. Si se quisieramos utilizar ese valor en Kelvin para otra operacion, no se podria porque la funcion no "devuelve" nada.

# --- Ejercicio 2 corregido ---

def celsius_a_kelvin():
    # Se convierte la entrada de texto a número decimal
    celsius = float(input("Ingrese la temperatura en Celsius: "))
    kelvin = celsius + 273.15
    return kelvin

# Para usarla:
resultado = celsius_a_kelvin()
print(f"La temperatura en Kelvin es: {resultado}")

# ------------------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 3

# El siguiente código intenta concatenar un nombre con un número entero para crear un usuario, pero tiene varios problemas. Identificá por qué falla y proponé una solución.
funcion CrearUsuario(nombre, numero):
    usuario = nombre + numero
    return usuario


# Error --> Este problema presenta dos errores:
# 1. Error de sintaxis: El error principal es que en Python no se usa la palabra funcion, sino la palabra reservada def (de define)
# 2. Error logico: Hay un detalle logico, si numero llega como entero (int), el programa fallara al intentar sumarlo con nombre (string). Para evitar esto se debe convertir el numero a texto.


# --- Ejercicio 3 corregido ---

def crear_usuario(nombre, numero):
    usuario = nombre + str(numero)
    return usuario

# Ejercicio 16 - Función: eliminar todas las "a" de una palabra

# EJERCICIO DADO -- Analizar qué tipo de dato (o error) se obtiene al hacer las siguientes operaciones:

# 5 / 2
# 5 // 2
# 5 % 2
# 5 ** 2
# 5.0 / 2
# 5.0 // 2
# 5.0 % 2
# 5.0 ** 2
# 5 / 2.0
# 5 // 2.0
# 5 % 2.0
# 5 ** 2.0
# 5.0 / 2.0
# 5.0 // 2.0
# 5.0 % 2.0
# 5.0 ** 2.0
# "Hola" * 2
# "Hola" + 2
# "Hola" + "2"
# x = "Hola"
# x += " mundo" 


# Análisis de Operaciones Numéricas
# (5 / 2) # --> 2.5 -- float -- La división simple siempre devuelve decimales.
# (5 // 2) # --> 2 -- int -- Division entera (solo la parte de abajo).
# (5 % 2) # --> 1 -- int -- Módulo (el resto de la división).
# (5 ** 2) # --> 25 -- int -- Potencia (5 al cuadrado).
# (5.0 / 2) # --> 2.5 -- float -- Al haber float, el resultado es float.
# (5.0 // 2) # --> 2.0 -- float -- Divison entera, pero expresada como float.
# (5.0 % 2) # --> 1.0 -- float -- Resto expresado como float.
# (5.0 ** 2) # --> 25.0 -- float -- Potencia expresada como float.
# (5 / 2.0) # --> 2.5 -- float -- Al igual que arriba (un operando es float).
# (5 // 2.0) # --> 2.0 -- float -- El divisor float convierte el resultado a float.
# (5 % 2.0) # --> 1.0 -- float -- Resto como float.
# (5 ** 2.0) # --> 25.0 -- float -- Exponente como float, genera un float.
# (5.0 / 2.0) # --> 2.5 -- float -- Ambos son float.
# (5.0 // 2.0) # --> 2.0 -- float -- Ambos son float.
# (5.0 % 2.0) # --> 1.0 -- float -- Ambos son float.
# (5.0 ** 2.0) # --> 25.0 -- float -- Ambos son float.

# Análisis de Operaciones con Strings (Cadenas)
# ("Hola" * 2) # --> "HolaHola" -- str -- Replicación: Repite la cadena N veces.
# ("Hola" + 2) # --> ERROR -- TypeError -- No se puede sumar texto y número directamente. 
# ("Hola" + "2") # --> "Hola2" -- str -- Concatenación: Une dos cadenas de texto.
# (x = "Hola") # --> "Hola" -- str -- Asignación multiple.
# (x += " mundo") # --> "Hola mundo" -- str -- Asignación compuesta: Equivale a x = x + "mundo".


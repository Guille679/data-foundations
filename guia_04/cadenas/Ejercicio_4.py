# Ejercicio 4 - Subcadena, orden alfabético entre dos strings

# EJERCICIO DADO -- Escribir funciones que dadas dos cadenas de caracteres:

# Indique si la segunda cadena es subcadena de la primera.
# Devuelva la que sea anterior en orden alfábetico.

def EsSubcadena(grande, pequeña):
    if pequeña in grande:
        return True
    else:
        return False
    

def QuienVaPrimero(cadena1, cadena2):
    if cadena1.lower() < cadena2.lower():
        return cadena1
    else:
        return cadena2

# Ejemplos de uso:

# --- Prueba de Subcadena ---
print("--- Test Subcadena ---")
print(EsSubcadena("computacional", "compu"))    
print(EsSubcadena("algoritmos", "log"))         
print(EsSubcadena("python", "java"))            

# --- Prueba de Orden Alfabetico ---
print("\n--- Test Orden Alfabetico ---")
print(QuienVaPrimero("kde", "gnome"))           
print(QuienVaPrimero("Zebra", "abeja"))         
print(QuienVaPrimero("casa", "casamiento"))     
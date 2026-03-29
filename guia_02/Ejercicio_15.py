# Ejercicio 15 - Función: eliminar todas las "a" de una palabra

# EJERCICIO DADO -- Hacer una funcion que reciba una palabra, le borre todas las letras “a” e imprima el resultado por pantalla. 
# Pista: usar una función predefinida de Python. Ejemplo: Si se recibe “casa” se debe imprimir “cs”.

def eleminar_letra_a(palabra):
    resultado = palabra.replace("a", "").replace("A", "") # Dos replace para eliminar tanto minisculas como mayusculas
    return resultado

# Ejemplo de uso
test = "casa"
print(eleminar_letra_a(test))


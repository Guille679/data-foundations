# Ejercicio 14 - Función: slicing — primeros 5 chars, posiciones pares, palabra invertida 

# EJERCICIO DADO -- Hacer una función que reciba una palabra y que imprima los primeros 5 caracteres únicamente. 
# Ejemplo: Si se recibe “pensamiento” se debe imprimir “pensa”.
# Hacer una función que reciba una palabra y que imprima sólo los caracteres ubicados en posiciones pares. 
# Ejemplo: Si se recibe “pensamiento” se debe imprimir “pnaino”.
# Hacer una función que reciba una palabra y que imprima la palabra dada vuelta. 
# Ejemplo: Si se recibe “materia” se debe imprimir “airetam”.


def primero_cinco(palabra):
    
    # El rango es [inicio : fin]
    return palabra[:5]
    
def caracteres_pares(palabra):
    
    # El rango es [inicio : fin : paso]
    return palabra[::2]

def invertir_palabra(palabra):
    
    # El paso -1 invierte el orden
    return palabra[::-1]
    
# Ejemplo de uso

# Se guardan los resultados en variables
resultado1 = primero_cinco("pensamiento")
resultado2 = caracteres_pares("pensamiento")
resultado3 = invertir_palabra("materia")

# Se muestran todos
print(resultado1) # Imprime: pensa
print(resultado2) # Imprime: pnaino
print(resultado3) # Imprime: airetam
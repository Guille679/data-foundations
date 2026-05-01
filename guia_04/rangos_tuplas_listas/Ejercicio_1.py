# Ejercicio 1 - Operaciones con `range`

# EJERCICIO DADO -- Usar un rango para:

# Imprimir los números del 10 al 50 inclusive, saltando de 5 en 5.
# Imprimir los números del 40 al 20 en orden decreciente, saltando de 2 en 2.

# Crear una lista con los números del 4 al 10. Luego, acceder con el índice a los elementos que contienen a los números 4, 6 y 9 e impimirlos por pantalla. Pista: recordar que los índices comienzan en 0.

# Primera parte (10 al 50 inclusive)
for numero in range(10, 51, 5): 
    print(numero)

# Segunda parte (40 al 20 decreciente inclusive)
for numero in range(40, 19, -2): 
    print(numero)

# Tercera parte (Numeros del 4 al 10)
mi_lista = list(range(4, 11)) # Usar list() para que se comporte como una lista real

# Ejemplo de uso
print(mi_lista[0]) # Imprime 4
print(mi_lista[2]) # Imprime 6
print(mi_lista[5]) # Imprime 9



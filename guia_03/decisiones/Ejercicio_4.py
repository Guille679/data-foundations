# Ejercicio 4 - Función: detectar vocal / consonante (con y sin `in`)

# EJERCICIO DADO -- Escribir una función para determinar si una letra recibida es vocal o no. La misma debe devolver un valor booleano. 
# Luego, escribir una función para determinar si una letra es consonante o no.
# Resolver sin el uso de in ni not in.
# Resolver usando in y not in.
# Resolver para que la función identifique tanto mayúsculas como minúsculas.

def es_vocal(letra):
    # Pasar a minuscula para que funcione con 'A' o 'a'
    letra_min = letra.lower()
    vocales = "aeiou"
    
    # Verificar si la letra está dentro de nuestra cadena de vocales
    if letra_min in vocales:
        return True
    else:
        return False

def es_consonante(letra):
    letra_min = letra.lower()
    vocales = "aeiou"
    
    # Verificar que NO este en las vocales
    if letra_min not in vocales:
        return True
    else:
        return False

# Ejemplo de uso:

print(f"¿La 'A' es vocal?: {es_vocal('A')}")
print(f"¿La 'e' es vocal?: {es_vocal('e')}")
print(f"¿La 'z' es vocal?: {es_vocal('z')}")

print(f"¿La 'B' es consonante?: {es_consonante('B')}")
print(f"¿La 'i' es consonante?: {es_consonante('i')}")

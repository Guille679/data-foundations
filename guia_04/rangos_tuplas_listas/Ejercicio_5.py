# Ejercicio 5 - Fichas de dominó: encajan o no

# EJERCICIO DADO -- Escribir una función que reciba dos fichas de dominó y determine si encajan o no entre sí.

# Resolver teniendo en cuenta que las fichas se reciben con formato de tuplas.
# Resolver teniendo en cuenta que las fichas se reciben con formato de string.

# Primera parte 

def encajan_tuplas(ficha1, ficha2):
    if ficha1[0] == ficha2[0] or ficha1[0] == ficha2[1] or ficha1[1] == ficha2[0] or ficha1[1] == ficha2[1]:
        return True
    else:
        return False

# Segunda parte

def encajan_strings(f1, f2):
    # Separa por guion
    p1 = f1.split("-")
    p2 = f2.split("-")
    
    # Comparar si hay interseccion entre los numeros
    return any(p in p2 for p in p1)

# Ejemplos de uso

# Prueba con tuplas
t1 = (3, 4)
t2 = (5, 4)
print("¿Encajan las tuplas (3,4) y (5,4)?", encajan_tuplas(t1, t2))

# Prueba con strings
s1 = "3-4"
s2 = "5-4"
print("¿Encajan los strings '3-4' y '5-4'?", encajan_strings(s1, s2))

# Prueba con fichas que no encajan
print("¿Encajan '1-2' y '5-6'?", encajan_strings("1-2", "5-6"))


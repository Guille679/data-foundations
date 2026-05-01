# Ejercicio 3 - Control de cupo en un curso 

# EJERCICIO DADO -- Escribir una función que reciba una lista de nombres y un número, que representa el cupo. 
# La función debe devolver en una lista a los nombres que no pudieron entrar al curso por falta de cupo. 
# Ejemplo: chequear_cupo(['Agustina', 'Iara', 'Priscila', 'Sol', 'Lucía'], 3) debe devolver ['Sol', 'Lucía'].

# Modificar la función anterior para que devuelva únicamente a la última persona de la lista de la gente que pudo entrar. 
# Ejemplo: chequear_cupo(['Agustina', 'Iara', 'Priscila', 'Sol', 'Lucía'], 3) debe devolver 'Priscila', porque es la última que tuvo cupo.

# Primera parte

def chequear_sin_cupo(lista_nombres, cupo):
    if len(lista_nombres) > cupo:
        lista_fuera = lista_nombres[cupo:]
        return lista_fuera
    else:
        return []

# Segunda parte

def ultima_persona_con_cupo(lista_nombres, cupo):
    indice_ultimo = cupo - 1

    if len(lista_nombres) >= cupo and cupo > 0:
        persona = lista_nombres[indice_ultimo]
        return persona
    else:
        return "No se lleno el cupo"

# Ejemplos de uso

alumnos = ['Agustina', 'Iara', 'Priscila', 'Sol', 'Lucia']
limite = 3

# Prueba primera parte
quedaron_fuera = chequear_sin_cupo(alumnos, limite)
print("Se quedaron sin cupo:", quedaron_fuera)

# Prueba segunda parte
ultimo_admitido = ultima_persona_con_cupo(alumnos, limite)
print("Ultima persona en entrar:", ultimo_admitido)

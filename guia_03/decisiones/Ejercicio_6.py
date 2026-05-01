# Ejercicio 6 - Piedra, papel o tijera — la máquina siempre gana

# EJERCICIO DADO -- Piedra, papel o tijera: escribir un programa de “Piedra, papel o tijera” tal que sea imposible que el usuario gane. 
# El usuario debe ingresar R (piedra), P (papel), o T (tijera) y la computadora debe siempre ganarle. 
# Las ejecuciones son individuales: el usuario sólo ingresa una sola vez su jugada, el programa le gana, y la ejecución termina.

def determinar_ganador(jugada_usuario):
    # Pasar a mayúsculas para evitar errores
    jugada_usuario = jugada_usuario.upper()

    if jugada_usuario == "R":
        return "¡Papel! ¡Gané!"
    elif jugada_usuario == "P":
        return "¡Tijera! ¡Gané!"
    elif jugada_usuario == "T":
        return "¡Piedra! ¡Gané!"
    else:
        return "Esa jugada no está disponible."


# Ejemplo de uso:

print("¡Piedra (R), papel (P) o tijera (T)!")
print("--" * 30)
eleccion = input("Ingrese jugada: ")

resultado = determinar_ganador(eleccion)
print(resultado)

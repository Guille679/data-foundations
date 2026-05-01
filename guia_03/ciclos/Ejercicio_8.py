# Ejercicio 8 -  Máquina de juguetes con fichas

# EJERCICIO DADO -- Queremos modelar una máquina de sacar juguetes. Debemos hacer una función que reciba un número que representa la cantidad de fichas X
# que necesita la máquina para funcionar. Se debe imprimir un mensaje en pantalla que indique “Ingresá X fichas para comenzar”. 
# El usuario deberá ingresar entonces letras “F”, que representan a las fichas. Notar que si se ingresa algo distinto a “F”, se ignora.
# Se debe seguir solicitando fichas siempre que no se haya alcanzado la cantidad necesaria para funcionar. Cuando se haya alcanzado la cantidad necesaria, se debe imprimir un mensaje que indique “¡A jugar!”.

# Modificar el programa anterior para que vaya mostrando la cantidad de fichas que faltan para comenzar a jugar.


def maquina_juguetes(cantidad_necesaria):
    faltantes = cantidad_necesaria

    while faltantes > 0:
        # Pedir la entrada al usuario
        entrada = input(f"Ingresá {faltantes} fichas para comenzar: ")

        # Si es una "F" (mayúscula), descontamos una ficha
        if entrada == "F":
            faltantes -= 1
        
        # Si ingresa cualquier otra cosa, el bucle sigue 
        # sin restar nada (se ignora)

    print("¡A jugar!")

# Ejemplo de uso con 2 fichas
maquina_juguetes(2)

# Ejercicio 6 -  Manejo de contraseñas con intentos limitados

# EJERCICIO DADO -- Escribir un programa que contenga una contraseña inventada, que le pregunte al usuario la contraseña, y 
# no le permita continuar hasta que la haya ingresado correctamente.
# Modificar el programa anterior para que solamente permita una cantidad fija de intentos.
# Modificar el programa anterior para que sea una función que devuelva si el usuario ingresó o no la contraseña correctamente, mediante un valor booleano (True o False).



# Version 1
password_secreta = "python123"
intento = ""

while intento != password_secreta:
    intento = input("Ingrese la contraseña: ")
    if intento != password_secreta:
        print("Incorrecto. Intente de nuevo.")

print("¡Acceso concedido!")



print ("--"*30)
# Version 2
password_secreta = "python123"
intentos_maximos = 3
intentos_realizados = 0

while intentos_realizados < intentos_maximos:
    intento = input(f"Contraseña (Intento {intentos_realizados + 1}/{intentos_maximos}): ")
    
    if intento == password_secreta:
        print("¡Acceso concedido!")
        break # Salir del bucle si acerto
    else:
        intentos_realizados += 1
        print("Contraseña incorrecta.")

if intentos_realizados == intentos_maximos:
    print("Cuenta bloqueada. Demasiados intentos fallidos.")



print ("--"*30)
# Version 3
def validar_acceso(password_correcta, intentos_max):
    for i in range(intentos_max):
        intento = input(f"Ingrese su clave ({i + 1} de {intentos_max}): ")
        if intento == password_correcta:
            return True # Devuelve True y termina la función inmediatamente
    
    return False # Si el for termina sin acertar, devuelve False

# Ejemplo de uso:
password_inventada = "profe123"
fue_exitoso = validar_acceso(password_inventada, 3)

if fue_exitoso:
    print("Bienvenido al sistema.")
else:
    print("Error de autenticacion.")

# Ejercicio 4 - Agenda con búsqueda e inserción por consola

# EJERCICIO DADO -- Se tiene una agenda implementada como diccionario, que guarda nombres de personas y sus números de teléfono. 
# Escribir un programa que le pida al usuario que ingrese nombres.

# Si el nombre se encuentra en la agenda, debe mostrar el teléfono.
# Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.

#En ambos casos, El usuario puede utilizar la palabra “EXIT” para dejar de ingresar nombres.

def IniciarAgenda():
    agenda = {"Juan": "1234", "Ana": "5678"}

    while True:
        nombre = input("Ingrese un nombre (o 'EXIT' para salir): ")

        # Validacion de salida insensible a mayusculas
        if nombre.upper() == "EXIT":
            break
        
        if nombre in agenda:
            # Usar f-string para imprimir cualquier tipo de dato sin error
            print(f"El telefono de {nombre} es: {agenda[nombre]}")
        else:
            print("El nombre no existe")
            nuevo_tel = input(f"Ingrese el numero de telefono para {nombre}: ")
            agenda[nombre] = nuevo_tel
            print("Contacto guardado")

    print("Agenda cerrada")
    return agenda


# Ejemplo de uso

agenda_finalizada = IniciarAgenda()

print("\n--- RESUMEN DE LA AGENDA ---")
print(agenda_finalizada)
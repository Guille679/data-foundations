# Ejercicio 12 - ⭐ Desafío: corrector de exámenes

# EJERCICIO DADO -- Desafío (obligatorio):

# Escribir una función que dada la cantidad de ejercicios de un examen, y el porcentaje de ejercicios bien resueltos necesario para aprobar dicho examen, revise un grupo de exámenes.
# Para ello, en cada paso debe preguntarle al usuario la cantidad de ejercicios resueltos por el alumno, o pedirle que ingrese “*” para salir. 
# Debe mostrar por pantalla el porcentaje correspondiente a la cantidad de ejercicios resueltos respecto a la cantidad de ejercicios del examen y una leyenda que indique si aprobó o no.

# Adicional al punto anterior: imprimir un mensaje informándole al usuario la cantidad de ejercicios y el % de aprobación.
# Validar que el usuario siempre ingrese números positivos y menor o iguales a la cantidad de ejercicios del examen, o “*“. De lo contrario, mostrar un mensaje de error y volver a pedirle el dato al usuario.


def corregir_examenes(total_ejercicios, porcentaje_minimo):
    # Imprimir mensaje informando cantidad de ejercicios y % de aprobacion
    print(f"Examen de {total_ejercicios} ejercicios. Se aprueba con el {porcentaje_minimo}%")

    while True:
        entrada = input("Ingrese la cantidad de ejercicios resueltos (o '*' para salir): ")

        # Pedir "*" para salir
        if entrada == "*":
            print("Fin de la correccion.")
            break
        
        # Validar números positivos y menores o iguales al total
        # Intentar convertir a numero para validar
        if entrada.replace("-", "").isdigit(): # Check básico de numero
            resueltos = int(entrada)
            
            if 0 <= resueltos <= total_ejercicios:
                # Mostrar porcentaje respecto al total
                porcentaje_alumno = (resueltos * 100) / total_ejercicios
                print(f"Porcentaje obtenido: {porcentaje_alumno}%")
                
                # Indicar si aprobó o no
                if porcentaje_alumno >= porcentaje_minimo:
                    print("Resultado: APROBADO")
                else:
                    print("Resultado: DESAPROBADO")
            else:
                # Mensaje de error y volver a pedir
                print(f"Error: El numero debe ser positivo y no mayor a {total_ejercicios}")
        else:
            # Mensaje de error para entradas no numericas (excepto *)
            print("Error: Ingreso invalido. Ingrese un numero o '*'")

# Ejemplo de uso:
corregir_examenes(10, 70)

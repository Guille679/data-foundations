# Ejercicio 5 - Función: año bisiesto

# EJERCICIO DADO -- Escribir funciones que resuelvan los siguientes problemas:
# a) Dado un año, que devuelva si es bisiesto.
# b) Dado un mes y un año, que devuelva la cantidad de días correspondientes.
# c) Pedirle al usuario su día y mes de cumpleaños. El programa debe imprimir un mensaje indicando a qué signo corresponde el usuario.


# a) Función para año bisiesto
def es_bisiesto(anio):
    # Un año es bisiesto si es divisible por 400 
    # O si es divisible por 4 pero no por 100
    if (anio % 400 == 0) or (anio % 4 == 0 and anio % 100 != 0):
        return True
    return False

# b) Función para cantidad de días del mes
def dias_del_mes(mes, anio):
    # Meses con 31 días
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    # Meses con 30 días
    elif mes in [4, 6, 9, 11]:
        return 30
    # Caso especial: Febrero
    elif mes == 2:
        if es_bisiesto(anio):
            return 29
        else:
            return 28
    return "Mes no válido"

# c) Función para el signo del zodiaco
def obtener_signo(dia, mes):
    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        return "Aries"
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        return "Tauro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        return "Géminis"
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        return "Cáncer"
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return "Leo"
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return "Virgo"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return "Libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        return "Escorpio"
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        return "Sagitario"
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
        return "Capricornio"
    elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        return "Acuario"
    elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        return "Piscis"
    else:
        return "Fecha no válida"

# Ejemplo de uso:

# 1. Probar bisiesto y días del mes
anio_actual = 2026
mes_actual = 4
print(f"¿El {anio_actual} es bisiesto?: {es_bisiesto(anio_actual)}")
print(f"Días en el mes {mes_actual} del {anio_actual}: {dias_del_mes(mes_actual, anio_actual)}")

print("-" * 30)

# 2. Interacción con el usuario para el signo
print("Consulta tu Signo Zodiacal")
dia_usuario = int(input("Ingresa el día de tu cumpleaños (1-31): "))
mes_usuario = int(input("Ingresa el número de tu mes de cumpleaños (1-12): "))

mi_signo = obtener_signo(dia_usuario, mes_usuario)
print(f"Tu signo es: {mi_signo}")

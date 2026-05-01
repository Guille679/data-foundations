# Ejercicio 7 - Función: día de la semana dado el día del año

# EJERCICIO DADO -- Suponiendo que el primer día del año fue lunes, escribir una función que reciba un número con el día del año (de 1 a 366) y devuelva el día de la semana que le toca. 


def ObtenerDiaSemana(dia_del_año):
    # El primer dia es lunes
    # Usar resto de la division por 7 para saber el lugar en la semana
    # Ajustar restando 1 para que el calculo sea exacto.

    posicion_en_semana = (dia_del_año - 1) % 7

    if posicion_en_semana == 0:
        return "lunes"
    elif posicion_en_semana == 1:
        return "martes"
    elif posicion_en_semana == 2:
        return "miercoles"
    elif posicion_en_semana == 3:
        return "jueves"
    elif posicion_en_semana == 4:
        return "viernes"
    elif posicion_en_semana == 5:
        return "sabado"
    elif posicion_en_semana == 6:
        return "domingo"
    

# Ejemplo de uso:

numero_dia = int(input("Ingrese el numero del dia del año (1 - 366): "))
print("--" * 20)

if numero_dia >= 1 and numero_dia <= 366:
    resultado = ObtenerDiaSemana(numero_dia)
    print("El dia ", numero_dia, " es ", resultado)
else:
    print("Numero de dia invalido")
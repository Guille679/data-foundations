# Ejercicio 16 - Desafío: sistema de donantes de sangre (Donarg)

# EJERCICIO DADO -- Desafío (no obligatorio): Donarg (https://www.donarg.com.ar/) es un proyecto que nació con estudiantes de FIUBA con el fin de optimizar procesos tanto para donantes de sangre como para hospitales y servicios de hemoterapia. Formado por estudiantes y graduados universitarios comprometidos, fue galardonado con el primer puesto en la FIUBATON 2020 “Desafío Cuarentena” del FIUBA Consulting Club, destacándose entre más de 100 proyectos.

# Donarg necesita un sistema que permita filtrar una base de datos de posibles donantes de sangre, quedándose con los que cumplen los requisitos.

# La base contiene los siguientes datos de cada posible donante:

# Nombre
# Apellido
# Edad
# Peso
# Fecha de la última donación. Puede ser ‘None’ si nunca donó. Formato: (dia,mes,año)
# Fecha del último tatuaje. Puede ser ‘None’ si no tiene tatuajes. Formato: (dia,mes,año)
# Tipo de sangre. Puede ser ‘0+’, ‘0-’, ‘A+’, ‘A-’, ‘B+’, ‘B-’, ‘AB+’, ‘AB-’

# Los requisitos son:

# Tener entre 16 y 65 años
# Pesar más de 50 kilos
# Que hayan pasado 2 meses desde la última donación
# Que hayan pasado 6 meses desde el último tatuaje
# Se pide hacer una función que reciba una lista de diccionarios con la información de cada posible donante, y devuelva una lista con los que cumplen los requisitos.

# Se pide hacer una función que priorice a los donantes que tienen sangre tipo 0 (positivo y negativo) por sobre todos los A, B y AB (positivos y negativos); ya que son los que más se necesitan. La función debe recibir la lista de diccionarios con la información de cada posible donante ya filtrada por requisitos, y devolver una nueva lista ordenados de mayor a menor prioridad.

# Se pide hacer una función que reciba la lista de diccionarios con la información de cada posible donante ya filtrada por requisitos y ordenada por prioridad, que se quede con los que son 0+ y 0-, y los ordene por órden alfabético de apellido.

def cumple_requisitos(donantes):
    hoy = (30, 4, 2026)
    aptos = []

    for d in donantes:
        if not (16 <= d["edad"] <= 65):
            continue
        if d["peso"] <= 50:
            continue
        
        if d["ultima_donacion"] is not None:
            d_don, m_don, a_don = d["ultima_donacion"]
            meses_don = (hoy[2] - a_don) * 12 + (hoy[1] - m_don)
            if meses_don < 2:
                continue
        
        if d["ultimo_tatuaje"] is not None:
            d_tat, m_tat, a_tat = d["ultimo_tatuaje"]
            meses_tat = (hoy[2] - a_tat) * 12 + (hoy[1] - m_tat)
            if meses_tat < 6:
                continue
        
        aptos.append(d)
    return aptos

def priorizar_tipo_0(donantes_aptos):
    def criterio_prioridad(donante):
        if '0' in donante["tipo_sangre"]:
            return 0
        return 1
    
    return sorted(donantes_aptos, key=criterio_prioridad)

def filtrar_ceros_y_ordenar(donantes_priorizados):
    solo_ceros = []
    for d in donantes_priorizados:
        if '0' in d["tipo_sangre"]:
            solo_ceros.append(d)
    
    solo_ceros.sort(key=lambda x: x["apellido"])
    return solo_ceros

# Ejemplo de uso
base_donantes = [
    {"nombre": "Ana", "apellido": "Zubiri", "edad": 25, "peso": 60, "ultima_donacion": (1, 1, 2026), "ultimo_tatuaje": None, "tipo_sangre": "A+"},
    {"nombre": "Juan", "apellido": "Perez", "edad": 30, "peso": 70, "ultima_donacion": None, "ultimo_tatuaje": (1, 1, 2024), "tipo_sangre": "0-"},
    {"nombre": "Beto", "apellido": "Abad", "edad": 40, "peso": 80, "ultima_donacion": (1, 1, 2026), "ultimo_tatuaje": None, "tipo_sangre": "0+"}
]

aptos = cumple_requisitos(base_donantes)
priorizados = priorizar_tipo_0(aptos)
final = filtrar_ceros_y_ordenar(priorizados)

print(final)

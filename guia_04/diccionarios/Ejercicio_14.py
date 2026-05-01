# Ejercicio 14 - ⭐ Desafío: bonos laborales como porcentaje

# EJERCICIO DADO -- Desafío (obligatorio): Laura tiene una lista de diccionarios donde guarda el valor de todas las reviews laborales anuales que le hicieron. 
# La información de cada una es año, seniority en ese momento (trainee, junior, semisenior, senior), el sueldo en ese momento y el valor del bono de performance que le dieron. 
# La semana pasada le avisaron que por políticas de la empresa, los bonos ahora deben calcularse como un porcentaje de su sueldo.

# Laura quiere entonces actualizar sus diccionarios, para que en vez de guardar el monto exacto del bono, guarde el porcentaje que le corresponde.

# Hacer una función que reciba la lista de diccionarios, y para cada una de las reviews, modifique el valor del bono por el porcentaje correspondiente.

# Hacer una función que reciba la lista de diccionarios ya modificada y devuelva los años en los que Laura tuvo un bono mayor al 50% de su sueldo. 
# Restricción: usar filter y map.


def actualizar_bonos_a_porcentaje(lista_reviews):
    for review in lista_reviews:
        sueldo = review["sueldo"]
        monto_bono = review["bono"]
        
        # Calcular el porcentaje: (bono / sueldo) * 100
        porcentaje = (monto_bono / sueldo) * 100
        
        # Reemplazar el monto por el porcentaje calculado
        review["bono"] = porcentaje

def obtener_años_bono_alto(lista_reviews):
    # 1. Filtrar los diccionarios donde el bono es > 50
    reviews_altas = filter(lambda r: r["bono"] > 50, lista_reviews)
    
    # 2. Mapear para quedarnos solo con el valor del año
    años = map(lambda r: r["año"], reviews_altas)
    
    return list(años)

# Ejemplo de uso
reviews_laura = [
    {"año": 2019, "seniority": "junior", "sueldo": 1000000, "bono": 40000},     # 4%
    {"año": 2020, "seniority": "semisenior", "sueldo": 1500000, "bono": 900000}, # 60%
    {"año": 2021, "seniority": "senior", "sueldo": 2000000, "bono": 1200000}    # 60%
]

# Paso 1: Modificar la lista original
actualizar_bonos_a_porcentaje(reviews_laura)
print("Reviews actualizadas:", reviews_laura)

# Paso 2: Obtener años con bono > 50%
años_record = obtener_años_bono_alto(reviews_laura)
print("Años con bonos mayores al 50%:", años_record)

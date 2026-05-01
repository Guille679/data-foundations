# Ejercicio 11 - Promedio de notas por intento

# EJERCICIO DADO -- La profesora Llamell guarda las notas del parcial de Pensamiento Computacional en una lista de diccionarios. 
# Cada diccionario tiene la siguiente información: nombre, apellido, intento, nota.

# Los intentos pueden ser 1 (si es la primera vez que rinde el parcial) o 2 (si está en el recuperatorio).

# Se pide hacer una función que dada esta lista de diccionarios, se devuelva el promedio de las notas en la primera oportunidad de los alumnos.

# Generalizar la función anterior, para que también reciba el número de intento y se pueda devolver el promedio de cualquiera de los dos intentos.

def calcular_promedio_intento(lista_notas, numero_intento):
    suma_notas = 0
    contador_alumnos = 0
    
    for registro in lista_notas:
        if registro["intento"] == numero_intento:
            suma_notas += registro["nota"]
            contador_alumnos += 1
            
    # Evitar la división por cero si nadie rindió ese intento
    if contador_alumnos == 0:
        return 0
        
    return suma_notas / contador_alumnos

# Ejemplo de uso
notas_computacion = [
    {"nombre": "Lucas", "apellido": "Gómez", "intento": 1, "nota": 8},
    {"nombre": "Marta", "apellido": "Pérez", "intento": 1, "nota": 4},
    {"nombre": "Lucas", "apellido": "Gómez", "intento": 2, "nota": 7},
    {"nombre": "Ana", "apellido": "Díaz", "intento": 1, "nota": 9}
]

# Promedio de la primera oportunidad (Intento 1)
promedio_1 = calcular_promedio_intento(notas_computacion, 1)
print(f"Promedio primer intento: {promedio_1:.2f}")

# Promedio del recuperatorio (Intento 2)
promedio_2 = calcular_promedio_intento(notas_computacion, 2)
print(f"Promedio segundo intento: {promedio_2:.2f}")

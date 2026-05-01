# Ejercicio 13 - Maratonistas: ordenar por nombre y por tiempo

# EJERCICIO DADO -- Se quiere guardar información de un grupo de maratonistas. Se necesita guardar su nombre, DNI y todas las maratones que corrió. 
# Para esto último, se guardan: nombre de cada una, año, puesto y el tiempo que tardaron en correrlas (en minutos).

# Crear un diccionario de ejemplo que represente esta situación.
# Teniendo esta lista de diccionarios, ordenarlos alfabéticamente por el nombre de los maratonistas.
# Teniendo esta lista de diccionarios, ordenar las maratones en tiempo ascendente según el tiempo que tardaron en correrlas.

# 1. Diccionario de ejemplo (Lista de maratonistas)
maratonistas = [
    {
        "nombre": "Zulma",
        "dni": 111,
        "maratones": [
            {"nombre": "Chicago", "año": 2021, "puesto": 15, "tiempo": 240},
            {"nombre": "Boston", "año": 2022, "puesto": 20, "tiempo": 210}
        ]
    },
    {
        "nombre": "Adrian",
        "dni": 222,
        "maratones": [
            {"nombre": "New York", "año": 2020, "puesto": 5, "tiempo": 180},
            {"nombre": "Berlin", "año": 2023, "puesto": 10, "tiempo": 195}
        ]
    }
]

# 2. Ordenar maratonistas alfabeticamente por nombre
# Usar lambda para decirle que el criterio de orden es la clave "nombre"
maratonistas.sort(key=lambda m: m["nombre"])

# 3. Ordenar las maratones de cada corredor por tiempo ascendente
for maratonista in maratonistas:
    # Ordenar la lista interna de maratones por la clave "tiempo"
    maratonista["maratones"].sort(key=lambda x: x["tiempo"])

# Resultado para verificar 
print("Maratonistas ordenados por nombre:")
for m in maratonistas:
    print(f"Nombre: {m['nombre']}")
    print(f"Maratones ordenadas por tiempo: {m['maratones']}")
    print("-" * 20)

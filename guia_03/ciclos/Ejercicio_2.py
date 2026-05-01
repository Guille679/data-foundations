# Ejercicio 2 -  Función: tabla de multiplicar

# EJERCICIO DADO -- Se quiere hacer un programa para enseñar a los niños las tablas de multiplicar del 1 al 10. 
# Crear una función que reciba un número e imprima por pantalla la tabla de multiplicar de ese número.


def generar_tabla(numero):
    # Usamos f"" para insertar variables directamente entre llaves {}
    print(f"--- Tabla del {numero} ---")

    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Ejemplo de uso
numero_usuario = int(input("Escribe un número: "))
generar_tabla(numero_usuario)

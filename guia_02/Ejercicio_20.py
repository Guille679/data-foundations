# Ejercicio 20 - Desafío: área de un rectángulo por coordenadas

# EJERCICIO DADO --  Calcular el área de un rectángulo (alineado con los ejes x e y), dadas sus
# coordenadas x1, x2, y1,e y2. Nota: considerar que tiene que funcionar para cualquier cuadrado,
# independientemente de los cuadrantes en los que tenga sus vertices.


def calcular_area_rectangulo(x1, x2, y1, y2):
    
    # abs() asegura que la distancia sea positiva aunque x2 > x1
    base = abs(x1 - x2)
    altura = abs(y1 - y2)
    
    area = base * altura
    return area

# Ejemplo de uso:

# Un rectángulo entre x=2, x=5 (base 3) y y=-1, y=3 (altura 4)
resultado = calcular_area_rectangulo(2, 5, -1, 3)
print(f"El área del rectángulo es: {resultado}") # Debería dar 12

# Ejercicio 15 - ⭐ Desafío: buscador de ejercicios de la guía

# EJERCICIO DADO -- Desafío (obligatorio): Los estudiantes de la materia Pensamiento Computacional quieren crear un programa que les facilite la cursada. Uno de los problemas es que no se tiene fácil acceso a los enunciados de los ejercicios, porque la guía es larga y hay que scrollear mucho. 
# En el programa, la guía de ejercicios se guarda en un diccionario, donde cada clave es el número de guía y cada valor una lista con los enunciados de los ejercicios, cada uno en su posición correspondiente (la posición 0 de la lista sólo guarda None). Se quiere que el usuario que está usando el programa pueda acceder por pantalla a un enunciado puntual de una guía con sólo pedirlo (si existe). Para el problema mencionado, hacer una función o más que lo resuelva. 
# Usar los temas visto en la materia hasta el momento, en la forma que se considere mejor y siguiendo las buenas prácticas y convenciones enseñadas.

def obtener_enunciado(guia_ejercicios, num_guia, num_ejercicio):
    if num_guia not in guia_ejercicios:
        return "Error: La guia solicitada no existe."
    
    guia_seleccionada = guia_ejercicios[num_guia]
    
    if num_ejercicio <= 0 or num_ejercicio >= len(guia_seleccionada):
        return "Error: El numero de ejercicio no es valido para esta guia."
    
    enunciado = guia_seleccionada[num_ejercicio]
    
    if enunciado is None:
        return "Error: No hay un enunciado cargado en esa posicion."
        
    return enunciado

# Ejemplo de uso
guia_pc = {
    "1": [None, "Hola mundo", "Hacer una suma", "Hacer un promedio"],
    "2": [None, "Definir una funcion", "Usar un if", "Explicar diccionarios"]
}

g = "1"
e = 2
resultado = obtener_enunciado(guia_pc, g, e)
print(resultado)

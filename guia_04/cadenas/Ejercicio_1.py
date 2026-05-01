# Ejercicio 1 - Insertar / reemplazar caracteres en un string

# EJERCICIO DADO -- Escribir funciones que dada una cadena y un caracter:

# Inserte el caracter entre cada letra de la cadena. Ejemplo: 'separar' y '-' debería devolver 's-e-p-a-r-a-r'.
# Reemplace todos los espacios por el caracter. Ejemplo: 'mi archivo de texto.txt' y '_’ debería devolver 'mi_archivo_de_texto.txt'.
# Reemplace todos los dígitos de la cadena por el caracter. Ejemplo: 'su clave es: 1540' y '*' debería devolver 'su clave es: ****'.
# Inserte el caracter cada 3 dígitos en la cadena. Ejemplo: '2552552550' y '.' debería devolver '255.255.255.0'
# Modificar todas las anteriores para que, adicionalmente, reciba un parámetro que indique la cantidad máxima de reemplazos o inserciones a realizar. Ejemplo: 'su clave es: 1540', '*' y 3 debería devolver 'su clave es: ***0'.

def insertar_entre(cadena, caracter, limite=None):
    resultado = ""
    largo = len(cadena)
    inserciones = 0
    for i in range(largo):
        resultado += cadena[i]
        if i < largo - 1:
            if limite is None or inserciones < limite:
                resultado += caracter
                inserciones += 1
    return resultado

# Ejemplo de uso:

# Sin límite
print(insertar_entre("separar", "-")) 
# Salida: s-e-p-a-r-a-r

# Con límite de 3 inserciones
print(insertar_entre("separar", "-", 3)) 
# Salida: s-e-p-a-rar



def reemplazar_espacios(cadena, caracter, limite=None):
    resultado = ""
    cambios = 0
    for letra in cadena:
        if letra == " ":
            if limite is None or cambios < limite:
                resultado += caracter
                cambios += 1
            else:
                resultado += letra
        else:
            resultado += letra
    return resultado

# Ejemplo de uso:

# Sin límite
texto_archivo = "mi archivo de texto.txt"
print(reemplazar_espacios(texto_archivo, "_")) 
# Salida: mi_archivo_de_texto.txt

# Con límite de 1 reemplazo
print(reemplazar_espacios(texto_archivo, "_", 1)) 
# Salida: mi_archivo de texto.txt


def reemplazar_digitos(cadena, caracter, limite=None):
    resultado = ""
    cambios = 0
    for letra in cadena:
        if letra.isdigit():
            if limite is None or cambios < limite:
                resultado += caracter
                cambios += 1
            else:
                resultado += letra
        else:
            resultado += letra
    return resultado

# Ejemplo de uso: 

# Sin límite
clave = "su clave es: 1540"
print(reemplazar_digitos(clave, "*")) 
# Salida: su clave es: ****

# Con límite de 3 reemplazos
print(reemplazar_digitos(clave, "*", 3)) 
# Salida: su clave es: ***0


def insertar_cada_tres(cadena, caracter, limite=None):
    resultado = ""
    contador_digitos = 0
    inserciones = 0
    for i in range(len(cadena)):
        resultado += cadena[i]
        if cadena[i].isdigit():
            contador_digitos += 1
            if contador_digitos == 3 and i < len(cadena) - 1:
                if limite is None or inserciones < limite:
                    resultado += caracter
                    inserciones += 1
                    contador_digitos = 0
    return resultado

# Ejemplo de uso:

# Sin límite
ip_suave = "2552552550"
print(insertar_cada_tres(ip_suave, ".")) 
# Salida: 255.255.255.0

# Con límite de 2 inserciones
print(insertar_cada_tres(ip_suave, ".", 2)) 
# Salida: 255.255.2550

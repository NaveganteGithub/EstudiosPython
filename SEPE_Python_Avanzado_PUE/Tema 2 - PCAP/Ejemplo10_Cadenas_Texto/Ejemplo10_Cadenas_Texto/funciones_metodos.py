texto = "bienvenidos al curso de Python"

print(texto)

# Poner primera letra de la frase en mayuscula
print(texto.capitalize())

# Poner la primera letra de cada palabra en mayuscula
print(texto.title())

# frase en mayusculas
print(texto.upper())

# frase en minusculas
print(texto.lower())

# Retornar un valor booleano que indica si la cadena es alfanumerica (letras y numeros)
print("Alfanumerica:", texto.isalnum()) # False porque tiene espacios en blanco
print("Alfanumerica:", "caracola12345".isalnum())  # True

# Retornar un valor booleano que indica si la cadena es alfabetica (letras)
print("Alfabetica:", texto.isalpha()) # False porque tiene espacios en blanco
print("Alfabetica:", "caracola".isalpha())  #True
print("Alfabetica:", "caracola12345".isalpha())  #False
print("Alfabetica:", "12345".isalpha())  #False

# Retornar un valor booleano que indica si la cadena es numerica (numeros)
'''
    isdigit():

Este método devuelve True si todos los caracteres en la cadena son dígitos y hay al menos un carácter, de lo contrario devuelve False.

No considera otros caracteres numéricos como los subíndices y superíndices, ni los caracteres de dígitos de otros idiomas.

Funciona bien con cadenas que contienen números enteros, pero no necesariamente con números decimales o fraccionarios.
'''
print("Numerica:", texto.isdigit()) # False no tenemos ningun numero
print("Numerica:", "12345".isdigit()) # True
print("Numerica:", "12 345".isdigit()) # False
print("Numerica:", "12.345".isdigit()) # False

# isdecimal() solo caracteres 0-9 y permite unicode
'''
    isdecimal():

Este método devuelve True si todos los caracteres en la cadena son dígitos y hay al menos un carácter, de lo contrario devuelve False.
Es más estricto que isdigit(), ya que solo acepta caracteres que se consideran dígitos decimales en Unicode.

No acepta subíndices, superíndices ni otros caracteres numéricos, y solo acepta dígitos del 0 al 9.

En resumen, isdigit() es más permisivo y puede devolver True para caracteres numéricos no decimales, mientras que isdecimal() es más estricto y solo devuelve True para dígitos decimales estándar del 0 al 9.
'''
print("Numerica:", "12345".isdecimal()) # True
print("Numerica:", "12.345".isdecimal()) # False
print("Numerica:", "00011101".isdecimal()) # True

a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G

print(a.isdecimal()) # True
print(b.isdecimal()) # False
print(a.isdigit()) # True

# Retorna un valor booleano indicando si el texto esta en minusculas
print("Minusculas:", texto.islower())  # False por la P de Python
print("Minusculas:", "hola".islower()) # True
print("Minusculas:", "hola12345".islower()) # True
print("Minusculas:", "12345hola".islower()) # True

# Retorna un valor booleano indicando si el texto esta en mayusculas
print("Mayusculas:", texto.isupper())  # False solo la P de Python es mayuscula
print("Mayusculas:", "HOLA".isupper()) # True
print("Mayusculas:", "HOLA12345".isupper()) # True
print("Mayusculas:", "12345HOLA".isupper()) # True

# lstrip -> elimina espacios por la izquierda
# rstrip -> elimina espacios por la derecha
# strip -> elimina espacios izquierda y derecha
ejemplo = "   hola   caracola     "
print(ejemplo.lstrip(), end=".\n")  # Por defecto elimina espacios
print("******hola   caracola     ".lstrip('*'), end=".\n")  # eliminar *

print(ejemplo.rstrip(), end=".\n")
print("******hola   caracola******".rstrip('*'), end=".\n")

print(ejemplo.strip(), end=".\n")
print("******hola   caracola******".strip('*'), end=".\n")

# Longitud de la cadena
# Funciones universales, nativas o Built-in
print("Longitud:", len(texto))
print("Longitud:", texto.__len__())

# Valor maximo y valor minimo
# En la tabla el orden es: numeros, mayusculas, minusculas
print("Max:", max(texto))  # y
print("Max:", max("aaaAAAAbbBB09"))  # b
print("Max:", max("AAAABB09"))  # B
print("Max:", max("aaabb09"))  #b
print("Max:", max("aaaAAAAbbBB"))  #b

print("Min:", min(texto))  # espacio
print("Min:", min("aaaAAAAbbBB09"))  # 0
print("Min:", min("AAAABB09"))  # 0
print("Min:", min("aaabb09"))  # 0
print("Min:", min("aaaAAAAbbBB"))  # A

for i in range(256):  # La tabla ASCII va desde 0 hasta 255
    print(i, ':', chr(i)) # retorna el caracter correspondiente a ese numero en la tabla ASCII

# Reemplazar texto
print("Reemplazar:", "abracadabra".replace('a','A')) # Reemplaza todas
print("Reemplazar:", "abracadabra".replace('a','A', 1))  # Solo la primera
print("Reemplazar:", "abracadabra".replace('a','A', 2))  # Solo las dos primeras
print("Reemplazar:", "abracadabra".replace('a','A', -1)) # AbrAcAdAbrA

# Retornar todas las palabras en una lista
print("lista:", texto.split())  # por defecto es el espacio en blanco
print("lista:", "9/4/2024".split('/'))

# Intercambiar mayusculas por minisculas
print("Swapcase:", "Hola, Que Tal?".swapcase())



# contar cuantas letras o tengo en mi texto
print("Cuantas o?", texto.count('o'))
print("Cuantas o a partir del indice 20?", texto.count('o', 20))
print("Cuantas o entre el indice 8 y 20?", texto.count('o', 8, 20))

# chr(): Devuelve el caracter asociado al numero que pasamos como argumento en la tabla ASCII
print(chr(200)) # È

# ord(): Le pasamos un caracter y me devuelve su posicion en la tabla ASCII
print(ord('È'))  # 200

#sort()
cadena = "abracadabra"
#cadena.sort() no existe en str
print(cadena)

#sorted()
cadena = "abracadabra"
print(sorted(cadena))
print(sorted(cadena, reverse=True))
print(cadena)

# Devuelve un valor booleano indicando si la cadena comienza por ese caracter
print(cadena.startswith('m'))  # False
print(cadena.startswith('a'))  # True
print(cadena.startswith('a', 5)) # True
print(cadena.startswith('a', 1, 3)) # False

# Devuelve un valor booleano indicando si la cadena termina por ese caracter
print(cadena.endswith('m'))  # False
print(cadena.endswith('a'))  # True
print(cadena.endswith('a', -3, -2)) # False
print(cadena.endswith('a', -1)) # True

# find busca por la izquierda y rfind busca comenzando por la derecha y retorna la posicion
print("Primera letra a:",cadena.find('a'))
print("Primera letra a partir del indice 5:",cadena.find('a', 5))
print("Primera letra a del indice 5 al 8:",cadena.find('a', 5, 8))

print("Ultima letra a:",cadena.rfind('a'))
print("Ultima letra a:",cadena.rfind('a', -4, -1))

# Unir los elementos de una coleccion con el caracter indicado y retorna un string
#print(" | ".join((range(5))))  # Error porque solo admite listas de cadenas
print(" | ".join(['a','e','i','o','u']))
print(" - ".join(['a','e','i','o','u']))

formato_numero_factura = ("Nº 0000-0", "-0000 (ID: ", ")")   #es una tupla de strings
print("275".join(formato_numero_factura))                    #275 es el separador, lo utiliza para unir cada elemento de la tupla

for i  in range(200,209):                          #del 200 al 209 son separadores
    print(str(i).join(formato_numero_factura))

# Retorna un booleano indicando si es un espacio o no
print(cadena.isspace()) # False
print(" ".isspace()) # True
print("\n".isspace()) # True
print("\t".isspace()) # True
print("".isspace()) # False

# muestra la cadena centrada en el numero de caracteres indicado y lo rellena con el caracter indicado
print(cadena.center(30, '.'))

fruta = "platano"
print(len(fruta))# 7
print(fruta.center(20, "O"))# OOOOOOplatanoOOOOOOO    longitud total 20 =  ( 6 ceros    7=platano  7 ceros )

# ejemplos utilizan codificación ascii y un carácter que no se puede codificar, mostrando el resultado con diferentes errores:
textoAcodificar = "Mi nombre es Ramb Ståle"
print(textoAcodificar.encode()) #b'Mi nombre es Ramb St\xc3\xa5le'
print(textoAcodificar.encode(encoding="ascii",errors="backslashreplace"))#b'Mi nombre es Ramb St\\xe5le'

# filter
cadena = "hola123"
digitos = filter(str.isdigit, cadena)
print(list(digitos))
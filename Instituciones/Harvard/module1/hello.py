# Ask user for their name
name = input("What´s your name? ") # input muestra un texto y despues pide un dato

# Say hello to user
"""
Is a
comment
on
five
lines
"""

print("hello, " + name) # Aqui pasas un argumento

"""
En las funciones de python cuando devuelven un valor en el cual 
son resultado de haber pasado varios argumentos agregan espacios 
en blanco entre valor y valor pasado por argumentos
"""


print("hello,", name) # Aqui pasas varios argumentos
print("hello, ", name)


# problema
print("hello, ")
print(name)

"""
end es un parametro predeterminado que me permite declarar como debe 
terminar una funcion, en este caso terminara con una cadena vacia
eliminando asi el salto de linea que hace por defecto el print
"""
print("hello, ", end="")
print(name)


"""
sep es un parametro predeterminado que me permite declarar que separadores o 
delimitadores tendra el texto
"""
print("hello,", name, sep='-')
print("hello,", name, name, sep='-')

# Para agregar comillas dentro de comillas
print('hello, "friend"')
print("hello, \"friend\"")

# Cadenas formatedas
print(f"hello, {name}")

""" 
strip me permite quitar espacios en blanco de la cadena dejando solo 
el primer espacio izquierdo y derecho si hubiera
"""
name = name.strip() 
print(f"hello, {name}")

""" 
capitalize me permite formatear el texto para cambiar al 
principio de la letra minuscula por la mayuscula
"""
name_aux = name # variable auxiliar
name = name.capitalize() 
print(f"hello, {name}")


"""
title me permite formatear el texto para cambiar todas las
palabras de la cadena para que empiecen por mayuscula
"""
name_aux_2 = name_aux
name_aux = name_aux.title() 
print(f"hello, {name_aux}")

# Se pueden combinar funciones
name = name_aux_2.strip().title()
print(f"hello, {name}")



name = input("What´s your name? ").strip().title()

""" 
Permite dividir el texto separado por un 
delimitador de una cadena en varias subcadenas 
y guardar dichas subcadenas variables, el numero
de subcadenas y el numero de variables tiene que
ser el mismo porque sino tirara error
"""
first, last = name.split(" ")
print(first)
print(last)
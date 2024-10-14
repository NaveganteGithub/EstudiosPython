# Esto es un comentario:
# Nuestro hola mundo en Python
print("Hola Python")
print('Hola Python')
# print(Hola Python) - Esto es un error

# La sintaxis de python no requiere de ;
# print sirve para imprimir

"""
Este es un
comentario
en varias líneas
"""

'''
Este es un
comentario
en varias líneas
'''

# Consultar el tipo de dato
# type("Hola Python")

print(type("Soy un dato str")) # Tipo str
print(type("Soy un dato int")) # Tipo str
print(type(5)) # Tipo int
print(type(1.5)) # Tipo float
print(type(3 + 1j)) # Tipo complex
print(type(True)) # Tipo bool

my_string_variable = "My String variable"
my_int_variable = 5
my_int_to_str_variable = str(my_int_variable)
my_bool_variable = False
print(type(print(my_string_variable, my_int_to_str_variable, my_bool_variable))) # Tipo NonType
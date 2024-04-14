# comparaciones

print("20" == 20)  # False
print("20" != 20)  # True
#print("20" >= 20)  # TypeError: '>=' not supported between instances of 'str' and 'int'
#print("20" <= 20)  # TypeError: '<=' not supported between instances of 'str' and 'int'
#print("20" > 20)  # TypeError: '>' not supported between instances of 'str' and 'int'
#print("20" < 20)  #TypeError: '<' not supported between instances of 'str' and 'int'

# operadores de pertenencia in y not in
cadena = "abracadabra"
print('m' in cadena) # False
print('b' in cadena) # True

print('m' not in cadena) # True
print('b' not in cadena) # False

# concatenar cadenas
# importante el orden
nombre = 'Pepito'
apellido = 'Perez'
nombre_completo = nombre + " " + apellido
nombre_completo = apellido + " " + nombre
print(nombre_completo)

# Interpolación de cadenas para insertar en una posición específica
cadena = "Hola Mundo"
posicion = 5
cadena = cadena[:posicion] + "Python " + cadena[posicion:]
print(cadena)  # Salida: "Hola Python Mundo"

# Repetir una cadena o caracter
print("hola" * 3)  # holaholahola
print('a' * 5) # aaaaa

# las multiplicaciones son conmutativas (el orden no afecta al producto)
print(5 * 'a') # aaaaa

# utilizamos a nivel comentario de bloque
''' docstring '''

# crear cadenas en varias lineas
nombre_completo = '''
    Pepito
    
    Perez
'''
print(nombre_completo)


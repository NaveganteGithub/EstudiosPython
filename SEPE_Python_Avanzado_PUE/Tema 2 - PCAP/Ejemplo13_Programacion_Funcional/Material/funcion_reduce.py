# la funcion reduce le pasamos un elemento iterable y retorna un solo resultado
# la funcion pasada como argumento ha de recibir:
#        - una variable que actua como acumulador
#        - El item recibido
# Sintaxis:   reduce(funcion, iterable)

''' Para utilizar reduce hay que importarlo'''
from functools import reduce

# Ejemplo 1
''' Con una lista de numeros devolver la suma '''
numeros = [3,8,2,1,7]

def sumar(acum, num):
    # la primera vez que se invoca a la funcion, el primer item se guarda como acumulador
    # y el segundo en num
    # Al realizar la suma el resultado se almacena en acum para siguientes iteraciones
    print(acum, num)
    return acum + num

print("Suma:", reduce(sumar, numeros))

# Ejemplo 2
'''con una lista de nombres, retornar una cadena con los nombres en mayuscula y separador por - '''
nombres = ["Luis", "Maria", "Juan"]

def concatenar(acum, nombre):
    return acum.upper() + " - " + nombre.upper()

print(reduce(concatenar, nombres))
# Modulos

'''
Los modulos en python tienen la finalidad
de crear bloques de codigo que se pueden
reutilizar, pero con la diferencia de que
estos se puede utilizar en cualquir proyecto

En Java tenemos las librerias, en Python los modulos

Los modulos son utililes pues:
    
    Nos premite la actualizacion contante del modulo
    de cierta forma que cuando se actualice la libreria
    en todos lo modulo podemos mejorar cosas
    
    Podemos evitar crecimiento de los errores en multiples
    proyectos por la copia constante de codigo
'''

'''
En funciones.py tenemos la funcion my_function(), que podiamos
reulizar tantas veces como queramos, una cosa clara esta en que
no podemos utilizar my_function aqui pues la funcion esta definida
en otro fichero
'''
# my_function()

'''
Todos los ficheros de python se comportara como modulos
'''
'''
def sum_two_values(first_number, second_number):
    print(first_number + second_number)
    
sum_two_values(5, 3)
'''


'''
import modulo # Primero se importa la libreria

modulo.sum(5, 3, 1) # Para luego usarla
'''


'''
Los modulos deben tener una sintaxis a la hora de escribir el nombre
no tiene que haber - , tampoco " "
'''


'''
import mi_modulo # Primero se importa la libreria

mi_modulo.sum(5, 3, 1) # Para luego usarla
modulo.printValue("Hola")
'''

'''
Se puede llamar de un modulo a un funcion,
para evitar llamar todos los componentes
'''

'''
from mi_modulo import sum

sum(5, 3, 1)
'''

from modulo import sumValue, printValue

sumValue(5, 3, 1)
printValue("Hola")


'''
Podemos invocar modulos que tenemos ya en el entorno de Python
'''
'''
import math

print(math.pi)

print(math.sqrt(4))

'''

'''
from math import pi
print(pi)
'''

from math import pi as PI_VALUE
print(PI_VALUE)
# print(pi) # Este da error
''' Diferentes formas de utilizar modulos '''

# primera forma importamos todo el modulo
import math

# Sintaxis: modulo.recurso
print("PI:", math.pi)

import math as m, string as s

# segunda forma
from math import pi
print("PI:", pi)

# tercera forma
from math import pi as num_pi

print("PI:", num_pi)


''' Importar mas de un recurso '''
from math import pi, e
print("PI:", pi)
print("E:", e)

from math import pi as num_pi, e as num_e
print("PI:", num_pi)
print("E:", num_e)

''' Para importar todo el modulo '''
from math import *

# no necesitamos poner por delante el nombre del modulo
print("PI:", pi)
print("E:", e)

# mostrar el contenido de un modulo
import math

print(dir(math))

for recurso in dir(math):
    print(recurso)
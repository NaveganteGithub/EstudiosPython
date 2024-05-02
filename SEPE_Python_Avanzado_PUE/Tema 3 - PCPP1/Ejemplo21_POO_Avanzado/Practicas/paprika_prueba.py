from paprika import to_string
from paprika import equals_and_hashcode
from paprika import data
from paprika import singleton

"""
Apunte importante, en python debes de tener cuidado a la hora 
de nombrar tus scripts, porque si nombras un script de python
igual que una libreria que estes importante te puede dar esta
excepcion o una parecida

ImportError: cannot import name 'to_string' from partially initialized 
module 'paprika' (most likely due to a circular import)
"""

"""@to_string                      # genera __str__
@equals_and_hashcode            # genera __eq__ y __hash__
@singleton                      # genera __init__(dia,mes,anyo)"""
@data                           # @data engloba los 3 decoradores anteriores
class FechaEncapsulada:
    
    dia: int
    mes: int
    anyo: int
       
fecha_buena = FechaEncapsulada(22, 4, 2024)
print(fecha_buena)

fecha_erronea = FechaEncapsulada(-12, 54, 3)
print(fecha_erronea)

fecha_erronea.dia = -12  # setter de dia
fecha_erronea.mes = 54
fecha_erronea.mes=10
#fecha_erronea.mes(8)  # TypeError: 'int' object is not callable
print(fecha_erronea)

print("Dia:", fecha_buena.dia)  # getter de dia

fecha_1 = FechaEncapsulada(23, 4, 2024)
fecha_2 = FechaEncapsulada(23, 4, 2024)

print(fecha_1 == fecha_2)
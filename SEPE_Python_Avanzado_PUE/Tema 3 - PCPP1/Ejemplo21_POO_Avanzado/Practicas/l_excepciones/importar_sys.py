import sys

try:
    print(7/0)
except ZeroDivisionError as excepcion:
    nombre, contexto, traza = sys.exc_info()
    print(nombre)
    print(contexto)
    print(traza)
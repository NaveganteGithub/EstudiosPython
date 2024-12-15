"""Elevar PI a la potencia
pasada por el parámetro
"""
from math import pi, inf

def potencia_pi(potencia):
    if potencia == inf:
        raise ArithmeticError

    return pi ** potencia

print(potencia_pi(5))
print(__doc__)
from math import pi, inf

def potencia_pi(potencia):
    """Elevar PI a la potencia pasada por el parámetro

        Keyword arguments:
        :param potencia: Potencia que elevara pi
        :type potencia: Union[int, double]
        :returns: retorna pi elevado a "potencia"
        :rtype: float
        :raises: TypeError: No se puede elevar pi con un carácter
        :raises: OverflowError: La potencia es demasiado alta, sobrecarga de RAM
        :raises: ArithmeticError: Pi por Infinito da Infinito
    """
    if potencia == inf:
        raise ArithmeticError

    return pi ** potencia

print(potencia_pi(5))
print(potencia_pi.__doc__)
print(potencia_pi.__code__)

help(potencia_pi)
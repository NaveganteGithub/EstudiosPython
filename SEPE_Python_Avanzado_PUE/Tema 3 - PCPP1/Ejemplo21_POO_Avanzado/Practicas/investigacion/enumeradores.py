"""
Un enumerador es una estructura de datos inmutable que va
contener un listado de nombres en el que cada nombre va
asociado a un valor que sera constante.
"""

from enum import Enum

class MiEnumerador(Enum):

    CONSTANTEUNO: list = 57
    CONSTANTEDOS: list = 4
    CONSTANTETRES: list = 12

    # Podemos declarar listas como constantes, pero tienen
    # tanta versatilidad como los datos primitivos
    """
    CONSTANTEUNO: list = [5, 8, 9, 7, 8, 9, 1]
    CONSTANTEDOS: list = [4, 4, 4, 4, 4, 4, 4]
    CONSTANTETRES: list = [1, 2, 3, 4, 5, 6, 7]
    """

print("He llamado a la CONSTANTEUNO", MiEnumerador.CONSTANTEUNO, sep=" ----- ")
print("He pedido el nombre de la CONSTANTEUNO", MiEnumerador.CONSTANTEUNO.name, sep=" ----- ")
print("He pedido el valor de la CONSTANTEUNO", MiEnumerador.CONSTANTEUNO.value, sep=" ----- ")

print("He llamado a la CONSTANTEDOS", MiEnumerador['CONSTANTEDOS'], sep=" ----- ")
print("He pedido el nombre de la CONSTANTEDOS", MiEnumerador['CONSTANTEDOS'].name, sep=" ----- ")
print("He pedido el valor de la CONSTANTEDOS", MiEnumerador['CONSTANTEDOS'].value, sep=" ----- ")

print("Comparando CONSTANTETRES con CONSTANTETRES",
      MiEnumerador.CONSTANTETRES is MiEnumerador['CONSTANTETRES'], sep=" ----- ")
print("Comparando CONSTANTEUNO con CONSTANTETRES",
      MiEnumerador.CONSTANTEUNO is MiEnumerador['CONSTANTETRES'], sep=" ----- ")

print("Buscar la constante a partir del valor 12", MiEnumerador(12), sep=" ----- ")
print("Buscar la constante a partir del valor 4", MiEnumerador(4), sep=" ----- ")

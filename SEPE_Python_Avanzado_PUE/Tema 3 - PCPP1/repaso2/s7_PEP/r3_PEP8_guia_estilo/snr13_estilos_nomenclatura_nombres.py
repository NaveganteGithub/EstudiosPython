# Regla 1 no uses nombres cortos como a o b

c = 0
contador = 0

# Regla 2 no uses como nombre la letra L (l en mayúscula), la letra I (i en mayúscula)
# y la letra O (o en mayúscula), estas letras se pueden hacer pasar por unos y ceros
# por la tipografía, lo que hará menos legible tu código

L = 1
I = 1
O = 0

# Regla 3: cuando uses acrónimos, tienes que escribir el nombre completo con la mayúscula del acrónimo

class PythonEnhancementProposalsEight:
    pass

# Regla 4: cada componente del código tiene su manera de ser nombrado

# snake_case

## Variables

coche = ""
marca_coche = ""

## Constantes

EMPRESA = ""
EMPRESA_COCHE = ""

## Nombres de modulos

### Si tienes un archivo llamado frutas.py
### import frutas
### Si tienes un archivo llamado frutas_tropicales.py
### import frutas_tropicales

## Funciones y métodos

def logaritmo():
    pass

def logaritmo_base_dos():
    pass

class Python:
    pass

class PythonEnhancementProposals:

    def __init__(self, identificador):
        self.identificador = identificador

    def enlace_pep(self):

        peps = {1: "https://peps.python.org/pep-0001/",
                8: "https://peps.python.org/pep-0008",
                20: "https://peps.python.org/pep-0020/",
                257: "https://peps.python.org/pep-0257/",
                484: "https://peps.python.org/pep-0484/"}

        return peps[self.identificador]

# CamelCase

## Clase

class Guia:
    pass

class GuiaDragonesCaballerosBosques:
    pass

## Variables de tipo: son variables con nombres del mismo tipo dato que la información que contiene,
## deben ser nombres cortos

TextoGenerico = "Hola"
Numero = 7

## Excepción

raise ValueError
raise TypeError
raise ArithmeticError
raise FileNotFoundError
raise FileExistsError

# minúsculas

## Paquete

## import alimentos.frutas
## import alimentossaludables.frutas

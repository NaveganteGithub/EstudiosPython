''' Crear una exception personalizada'''
import sys

"""class NegativoError(Exception):

    def __init__(self, *mensaje): # Podemos poner args en las excepciones personalizadas
        super().__init__(mensaje)"""

class NegativoError(Exception):

    def __init__(self, mensaje):
        self.menj = mensaje
    
    def __str__(self) -> str:
        return self.menj + ". Te recomiendo poner un valor igual o superior al minimo."

'''
edad = int(input("Introduce tu edad: "))
if edad < 0:
    # lanzar la excepcion de forma manual
    raise NegativoError("La edad no puede ser negativa")
'''

try:
    edad = int(input("Introduce tu edad: "))
    if edad < 0:
        # raise NegativoError("La edad no puede ser negativa", "Se necesita un numero positivo")
        raise NegativoError("La edad no puede ser negativa")
except NegativoError as ex:
    args, description, tb = sys.exc_info()
    #print(sys.exc_info())
    print(args)
    print("Mensaje", description)
    print("Traza", tb)
else:
    print("Edad positiva")

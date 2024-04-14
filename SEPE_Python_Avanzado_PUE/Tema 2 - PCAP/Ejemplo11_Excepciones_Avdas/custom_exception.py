''' Crear una exception personalizada'''
# Todas las excepciones en Python son clases que estan herando
# directa o indirectamente de la clase BaseException
# Nuestra excepcion personalizada sera una clase que herede de Exception

class NegativoError(Exception):  # NegativoError es una Exception
    def __init__(self, mensaje):
        #self.mensaje = mensaje
        super().__init__(mensaje)

    def getMensaje(self):
        return self.mensaje

edad = int(input("Introduce tu edad: "))
if edad < 0:
    # lanzar la excepcion de forma manual
    raise NegativoError("La edad no puede ser negativa")


'''
try:
    edad = int(input("Introduce tu edad: "))
    if edad < 0:
        # lanzar la excepcion de forma manual
        raise NegativoError("La edad no puede ser negativa")
except NegativoError as ex:
    print(ex.getMensaje())
else:
    print("Edad positiva")
'''



'''
Traceback (most recent call last):
  File "/Users/anaisabelvegascaceres/Desktop/python_avanzado_PUE_1_Abril/Ejemplo11_Excepciones_Avdas/custom_exception.py", line 12, in <module>
    raise NegativoError
__main__.NegativoError
'''


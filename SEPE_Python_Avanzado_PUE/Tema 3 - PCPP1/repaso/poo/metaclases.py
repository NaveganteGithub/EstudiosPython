
# Una metaclase es un objeto que nos permite definir
# el como estarán conformadas las clases en Python

class MiClase:

    def __init__(self, x):
        self.h = x

clase = MiClase(5)

print(type(clase)) # Nos devuelve el tipo de clase que conforma la instancia
print(type(MiClase)) # Nos devuelve la clase Padre de MiClase que es type (que es la metaclase)


def saludo():
    print("Hola")

mi_clase = type("MiClase2", (), {"atributo1": 2123, "metodo": saludo()})
print(mi_clase)
print(mi_clase.atributo1)
mi_clase.metodo


class MiMetaclase(type):

    def __new__(cls, nombre_clase, bases, atributos):
        print(nombre_clase, bases, atributos)
        return type(nombre_clase, bases, atributos)


class Clase(metaclass=MiMetaclase):

    def __init__(self, a):
        self.animal = a

    def imprimir(self):
        print("Hola", self.animal)


clase = Clase("Oso")
clase.imprimir()


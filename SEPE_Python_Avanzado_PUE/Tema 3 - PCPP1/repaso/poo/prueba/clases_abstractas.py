import abc

class Interfaz(abc.ABC):

    @classmethod
    @abc.abstractmethod
    def figura(cls, diametro):
        pass

class MiClase(Interfaz):

    def figura(self, diametro):
        return diametro * 4

clase = MiClase()
print(clase.figura(3))

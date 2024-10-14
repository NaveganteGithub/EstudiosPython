
import abc

class Platilla(abc.ABC):

    @classmethod
    @abc.abstractmethod
    def lk(cls, el):
        pass


class MiClase(Platilla):

    def asd(self):
        print("Hola")

    def lk(self, el):
        print("Adios")


clase = MiClase()
clase.asd()

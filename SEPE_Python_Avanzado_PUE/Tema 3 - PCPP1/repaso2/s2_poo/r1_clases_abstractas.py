import abc

# Las clases abstractas son plantillas (blueprints) que nos permiten
# definir una estructura inicial para las clases

# Ojo cuidado, ABC no es una metaclase es una clase
class ClasesAbstractas(abc.ABC):

    @classmethod
    @abc.abstractmethod
    def pasion(cls, nivel):
        pass


class MiClase(ClasesAbstractas):

    def __init__(self, amor, pasion):
        self.mi_amor = amor
        self.mi_pasion = pasion

    def pasion(self, nivel):
        return self.mi_pasion + nivel

    def amor(self, nivel):
        return self.mi_amor ** nivel

# En caso de no implementar todos los métodos de la clase abstracta dará un error
# TypeError: Can't instantiate abstract class MiClase without an implementation for abstract method 'pasion'
clase = MiClase(189, 185)
print(clase.pasion(5))
print(clase.amor(7))

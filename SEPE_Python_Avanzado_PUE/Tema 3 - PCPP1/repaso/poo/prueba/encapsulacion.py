
class MiClase:

    def __init__(self, x):
        self.horizontal = x

    @property
    def manejo_x(self):
        print("Get")
        return self.horizontal

    @manejo_x.setter
    def manejo_x(self, x):
        print("Set")
        self.horizontal = x

    @manejo_x.deleter
    def manejo_x(self):
        print("Eliminado")
        del self.horizontal


clase = MiClase(5)
print(clase.manejo_x)
clase.manejo_x = 4
print(clase.manejo_x)
del clase.manejo_x

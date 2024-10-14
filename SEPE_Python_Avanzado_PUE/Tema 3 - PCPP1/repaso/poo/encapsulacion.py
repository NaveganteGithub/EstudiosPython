from datetime import datetime

class MiClase:

    def __init__(self, registro, nombre, fecha):
        self.identificador = registro
        self.nombre = nombre
        self.fecha = fecha

    @property
    def manejar_id(self):
        return self.identificador

    @manejar_id.setter
    def manejar_id(self, registro):
        self.identificador = registro

    @manejar_id.deleter
    def manejar_id(self):
        print("Se ha eliminado el identificador")
        del self.identificador


clase = MiClase(5464655, "David", datetime(2005, 11, 25, 10, 12, 50, 1200))
print(clase.manejar_id)
clase.manejar_id = 4564564
print(clase.manejar_id)
del clase.manejar_id

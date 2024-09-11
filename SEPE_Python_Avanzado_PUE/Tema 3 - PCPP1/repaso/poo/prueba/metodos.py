
class MiClase:

    dia: int
    mes: int
    tiempo: int

    def __init__(self, dia, mes, tiempo):
        MiClase.dia = dia
        MiClase.mes = mes
        MiClase.tiempo = tiempo

    @staticmethod
    def datos():
        return MiClase.dia, MiClase.mes, MiClase.tiempo

    @classmethod
    def instancias(cls):
        return MiClase(5, 10, 2012)


print(MiClase.datos())
print(MiClase.instancias())
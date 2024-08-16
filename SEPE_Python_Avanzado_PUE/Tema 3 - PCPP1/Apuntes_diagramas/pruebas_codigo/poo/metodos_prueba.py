
class Nacimiento:

    dia: int
    mes: int
    tiempo: int

    def __init__(self, dia, mes, tiempo):
        Nacimiento.dia = dia
        Nacimiento.mes = mes
        Nacimiento.tiempo = tiempo

    @staticmethod
    def fecha_str():
        return f"{Nacimiento.dia} {Nacimiento.mes} {Nacimiento.tiempo}"

    @classmethod
    def fecha_obj(cls, dia, mes, tiempo):
        return Nacimiento(dia, mes, tiempo)


# Si te fijas ambos tienen algo en comun,
# y es que se acceden de la misma manera:
#
# Clase.metodo(p1, p2)
fecha = Nacimiento(20, 5, 2024)
print(Nacimiento.fecha_str())

fecha_2 = Nacimiento.fecha_obj(10, 2, 2024)
print(fecha_2.mes)
print(Nacimiento.mes)

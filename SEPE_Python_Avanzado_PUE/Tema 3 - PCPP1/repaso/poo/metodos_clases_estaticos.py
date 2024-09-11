
class MiClase:

    sal: int = None

    def __init__(self, sal):
        MiClase.sal = sal

    @classmethod
    def manejo_instancia(cls):
        return MiClase(5)

    @staticmethod
    def get_sal():
        return MiClase.sal

mi_instancia = MiClase.manejo_instancia()
print(mi_instancia.sal)

print(MiClase.get_sal())

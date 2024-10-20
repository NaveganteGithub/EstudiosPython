
class MisMetodos:

    def __init__(self, a, b):
        self.factor1 = a
        self.factor2 = b

    @classmethod
    def empaquetar(cls, *args):
        longitud = len(args)//2
        lista1 = args[:longitud]
        lista2 = args[longitud:]
        return MisMetodos(lista1, lista2)

    @staticmethod
    def calculo(a: int, b: int) -> int:
        return a + b

print(MisMetodos.empaquetar(1,5,6,8,4).factor1)
print(MisMetodos.calculo(5, 6))
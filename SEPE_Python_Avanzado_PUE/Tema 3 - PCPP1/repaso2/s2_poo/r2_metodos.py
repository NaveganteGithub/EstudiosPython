
class MisMetodos:

    def __init__(self, a, b):
        self.factor1 = a
        self.factor2 = b

    # Métodos de instancia
    def informacion_instancia(self):
        return self.factor1, self.factor2, dir(MisMetodos)[-3:]

    # Métodos estáticos
    @staticmethod
    def calculo(a: int, b: int) -> int:
        return a + b

    # Métodos de clase
    @classmethod
    def empaquetar(cls, *args):
        longitud = len(args) // 2
        lista1 = args[:longitud]
        lista2 = args[longitud:]
        return MisMetodos(lista1, lista2)

print(MisMetodos.empaquetar(1,5,6,8,4).factor1)
print(MisMetodos.calculo(5, 6))

metodos = MisMetodos(51,5)
print(metodos.informacion_instancia())

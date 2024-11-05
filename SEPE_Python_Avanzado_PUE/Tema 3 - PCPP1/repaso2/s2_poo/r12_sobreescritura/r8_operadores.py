
class Operadores:

    def __init__(self):
        self.numero = 5

    def __neg__(self):
        print("Negativo")
        return -self.numero

    def __pos__(self):
        print("Positivo")
        return +self.numero

clase = Operadores()
print(-clase)
print(+clase)
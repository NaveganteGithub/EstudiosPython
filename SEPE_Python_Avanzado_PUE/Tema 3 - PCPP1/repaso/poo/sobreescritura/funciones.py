
class Funciones:

    def __init__(self, n):
        self.numero = n

    def __abs__(self):
        return abs(self.numero)

    def __round__(self, n=None):
        return round(self.numero)

num = Funciones(5)

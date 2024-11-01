
class Funciones:

    def __init__(self, n):
        self.num = n

    def __abs__(self):
        print("Sobreescritura")
        return abs(self.num)

    def __round__(self):
        print("Sobreescritura")
        return round(self.num)

clase = Funciones(7.51215616)
print(abs(clase))
print(round(clase))

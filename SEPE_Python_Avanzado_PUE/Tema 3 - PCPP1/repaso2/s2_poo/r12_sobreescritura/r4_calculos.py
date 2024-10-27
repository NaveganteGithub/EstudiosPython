
class Calculos:

    def __init__(self, f):
        self.factor = f

    def __add__(self, other):
        return self.factor + other.factor

    def __sub__(self, other):
        return self.factor - other.factor

    def __mul__(self, other):
        return self.factor * other.factor

    def __truediv__(self, other):
        return self.factor / other.factor

    def __floordiv__(self, other):
        return self.factor // other.factor

    def __mod__(self, other):
        return self.factor % other.factor

    def __pow__(self, power, modulo=None):
        # return self.factor ** power
        return self.factor ** power.factor

clase = Calculos(50)
clase2 = Calculos(14)
print(clase + clase2)
print(clase - clase2)
print(clase * clase2)
print(clase / clase2)
print(clase // clase2)
print(clase % clase2)
# print(pow(clase, clase2))
print(clase ** clase2)
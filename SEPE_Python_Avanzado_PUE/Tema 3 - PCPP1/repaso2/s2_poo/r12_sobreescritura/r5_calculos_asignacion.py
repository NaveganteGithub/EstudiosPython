
class Calculos:

    def __init__(self, f):
        self.factor = f

    def __iadd__(self, other):
        return self.factor + other.factor

    def __isub__(self, other):
        return self.factor - other.factor

    def __imul__(self, other):
        return self.factor * other.factor

    def __itruediv__(self, other):
        return self.factor / other.factor

    def __ifloordiv__(self, other):
        return self.factor // other.factor

    def __imod__(self, other):
        return self.factor % other.factor

    def __ipow__(self, other):
        return self.factor ** other.factor


clase1 = Calculos(7)
clase2 = Calculos(5)
print(type(clase1))
clase1 += clase2
print(clase1)
print(type(clase1))

clase1 = Calculos(7)
clase2 = Calculos(5)
clase1 += clase2
print(clase1)

clase1 = Calculos(7)
clase2 = Calculos(5)
clase1 -= clase2
print(clase1)

clase1 = Calculos(7)
clase2 = Calculos(5)
clase1 *= clase2
print(clase1)

clase1 = Calculos(350)
clase2 = Calculos(5)
clase1 /= clase2
print(clase1)

clase1 = Calculos(350)
clase2 = Calculos(5)
clase1 //= clase2
print(clase1)

clase1 = Calculos(350)
clase2 = Calculos(5)
clase1 %= clase2
print(clase1)

clase1 = Calculos(7)
clase2 = Calculos(5)
clase1 **= clase2
print(clase1)

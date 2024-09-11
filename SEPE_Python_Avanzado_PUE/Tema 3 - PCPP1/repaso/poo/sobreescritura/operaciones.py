

class Operaciones:

    def __init__(self, num):
        self.numero = num

    def __add__(self, other):
        return self.numero + other.numero

    def __sub__(self, other):
        return self.numero - other.numero

    def __mul__(self, other):
        return self.numero * other.numero

    def __truediv__(self, other):
        return self.numero / other.numero

    def __floordiv__(self, other):
        return self.numero // other.numero

    def __mod__(self, other):
        return self.numero % other.numero

    def __pow__(self, power, modulo=None):
        return self.numero ** power.numero


factor1 = Operaciones(5)
factor2 = Operaciones(3)

print(factor1 + factor2)
print(factor1 - factor2)
print(factor1 * factor2)
print(factor1 / factor2)
print(factor1 // factor2)
print(factor1 % factor2)
print(factor1 ** factor2)

class Asignacion:

    def __init__(self, num):
        self.numero = num

    def __iadd__(self, other):
        self.numero += other.numero
        return self.numero

    def __isub__(self, other):
        self.numero -= other.numero
        return self.numero

    def __imul__(self, other):
        self.numero *= other.numero
        return self.numero

    def __itruediv__(self, other):
        self.numero /= other.numero
        return self.numero

    def __ifloordiv__(self, other):
        self.numero //= other.numero
        return self.numero

    def __imod__(self, other):
        self.numero %= other.numero
        return self.numero

    def __ipow__(self, other):
        self.numero **= other.numero
        return self.numero


factor1 = Asignacion(15)
factor2 = Asignacion(13)

"""factor1 += factor2
print(factor1)
factor1 -= factor2
print(factor1)
factor1 *= factor2
print(factor1)
factor1 /= factor2
print(factor1)
factor1 //= factor2
print(factor1)
factor1 %= factor2
print(factor1)"""
factor1 **= factor2
print(factor1)


class Uninarios:

    def __init__(self, num):
        self.numero = num

    def __pos__(self):
        print("Hola")
        return +self.numero

    def __neg__(self):
        print("Hola")
        return -self.numero

numero = Uninarios(-5)
print(+numero)
print(-numero)

class Calculos:

    def __init__(self, f1, f2):
        self.factor1 = f1
        self.factor2 = f2

    def __add__(self, other):
        return self.factor1 + other.factor1, self.factor2 + other.factor2

    def __sub__(self, other):
        return self.factor1 - other.factor1

    def __mul__(self, other):
        return self.factor1 - other.factor1

    def __truediv__(self, other):
        return self.factor1 / other.factor1

    def __floordiv__(self, other):
        return self.factor1 // other.factor1

    def __mod__(self, other):
        return self.factor1 % other.factor1

    def __pow__(self, other):
        return self.factor1 ** other.factor1


mi_calculo1 = Calculos(5, 2)
mi_calculo2 = Calculos(9, 2)

print(mi_calculo1 + mi_calculo2)
print(mi_calculo1 - mi_calculo2)
print(mi_calculo1 * mi_calculo2)
print(mi_calculo1 / mi_calculo2)
print(mi_calculo1 // mi_calculo2)
print(mi_calculo1 % mi_calculo2)
print(mi_calculo1 ** mi_calculo2)

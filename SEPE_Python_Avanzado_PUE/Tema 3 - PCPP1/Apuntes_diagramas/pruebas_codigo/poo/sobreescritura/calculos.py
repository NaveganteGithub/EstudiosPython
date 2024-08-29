
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


class Calculos_Asignacion:

    def __init__(self, f1, f2):
        self.factor1 = f1
        self.factor2 = f2

    def __str__(self):
        return f"{self.factor1} y {self.factor2}"

    def __iadd__(self, other):
        # Sorprendentemente, esto funciona
        # return self.factor1 + other.factor1, self.factor2 + other.factor2
        return self.factor1 + other.factor1

    def __isub__(self, other):
        return self.factor1 - other.factor1

    def __imul__(self, other):
        return self.factor1 * other.factor1

    def __itruediv__(self, other):
        return self.factor1 / other.factor1

    def __ifloordiv__(self, other):
        return self.factor1 // other.factor1

    def __imod__(self, other):
        return self.factor1 % other.factor1
    
    def __ipow__(self, other):
        return self.factor1 ** other.factor1


mi_asignacion_1 = Calculos_Asignacion(7, 3)
mi_asignacion_2 = Calculos_Asignacion(5, 1)

"""mi_asignacion_2 += mi_asignacion_1
print("SA", mi_asignacion_2)

mi_asignacion_2 -= mi_asignacion_1
print(mi_asignacion_2)

mi_asignacion_2 *= mi_asignacion_1
print(mi_asignacion_2)

mi_asignacion_2 /= mi_asignacion_1
print(mi_asignacion_2)

mi_asignacion_2 //= mi_asignacion_1
print(mi_asignacion_2)

mi_asignacion_2 %= mi_asignacion_1
print(mi_asignacion_2)"""

mi_asignacion_2 **= mi_asignacion_1
print(mi_asignacion_2)

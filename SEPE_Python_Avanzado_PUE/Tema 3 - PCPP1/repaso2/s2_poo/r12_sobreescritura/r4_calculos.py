
class Calculos:

    def __init__(self, f):
        self.factor = f

    def __add__(self, other):  # Modifica el comportamiento del Operador Suma
        print(f"{self.factor} + {other.factor} = ", end="")
        return self.factor + other.factor

    def __sub__(self, other):  # Modifica el comportamiento del Operador Resta
        print(f"{self.factor} - {other.factor} = ", end="")
        return self.factor - other.factor

    def __mul__(self, other):  # Modifica el comportamiento del Operador Multiplicación
        print(f"{self.factor} * {other.factor} = ", end="")
        return self.factor * other.factor

    def __truediv__(self, other):  # Modifica el comportamiento del Operador División con coma flotante
        print(f"{self.factor} / {other.factor} = ", end="")
        return self.factor / other.factor

    def __floordiv__(self, other):  # Modifica el comportamiento del Operador División sin coma flotante
        print(f"{self.factor} // {other.factor} = ", end="")
        return self.factor // other.factor

    def __mod__(self, other):  # Modifica el comportamiento del Operador Módulo
        print(f"{self.factor} % {other.factor} = ", end="")
        return self.factor % other.factor

    def __pow__(self, power, modulo=None):  # Modifica el comportamiento del Operador Potencia
        print(f"{self.factor} ** {power.factor} = ", end="")
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
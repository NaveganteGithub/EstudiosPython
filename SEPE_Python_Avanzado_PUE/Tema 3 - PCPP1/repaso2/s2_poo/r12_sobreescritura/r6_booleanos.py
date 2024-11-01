
class Booleanos:

    def __init__(self, e):
        self.edad = e

    def __eq__(self, other):
        return self.edad == other.edad

    def __ne__(self, other):
        return self.edad != other.edad

    def __gt__(self, other):
        return self.edad > other.edad

    def __ge__(self, other):
        return self.edad >= other.edad

    def __lt__(self, other):
        return self.edad < other.edad

    def __le__(self, other):
        return self.edad <= other.edad

clase = Booleanos(18)
clase2 = Booleanos(15)

print(clase == clase2)
print(clase != clase2)
print(clase > clase2)
print(clase >= clase2)
print(clase < clase2)
print(clase < clase2)

print()

clase = Booleanos(18)
clase2 = Booleanos(18)

print(clase == clase2)
print(clase != clase2)
print(clase > clase2)
print(clase >= clase2)
print(clase < clase2)
print(clase < clase2)
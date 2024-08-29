
# Esto es curioso, resulta que la recursividad
# no afecta en nada a los metodos abs y round.

class Operaciones:

    def __init__(self, n):
        self.num = n

    def __abs__(self):
        print("Hola")
        return abs(self.num)

    def __round__(self, n=2):
        print("Hola")
        return round(self.num, n)


funcion = Operaciones(-8.1556446)

print(abs(funcion))
print(round(funcion, 5))

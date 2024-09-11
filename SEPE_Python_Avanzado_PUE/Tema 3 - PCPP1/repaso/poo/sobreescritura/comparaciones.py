

class Comparaciones:

    def __init__(self, valor):
        self.valor = valor

    def __eq__(self, other):
        return self.valor == other.valor

    def __ne__(self, other):
        return self.valor != other.valor

    def __gt__(self, other):
        return self.valor > other.valor

    def __ge__(self, other):
        return self.valor >= other.valor

    def __lt__(self, other):
        return self.valor < other.valor

    def __le__(self, other):
        return self.valor <= other.valor


texto1 = Comparaciones("Hola buenas tardes")
texto2 = Comparaciones("Hola buenas")
numero1 = Comparaciones(3)
numero2 = Comparaciones(5)
print(texto1 == texto2)
print(texto1 != texto2)
print(numero1 > numero2)
print(numero1 >= numero2)
print(numero1 < numero2)
print(numero1 <= numero2)

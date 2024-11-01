

class Sabor:

    def imprimir(self):
        print(f"Sabor")

class Acido(Sabor):

    def imprimir(self):
        print(f"Sabor Acido")

class Dulce (Acido):

    def imprimir(self):
        print(f"Sabor Dulce")

sabor = Sabor()
acido = Acido()
dulce = Dulce()

sabor.imprimir()
acido.imprimir()
dulce.imprimir()

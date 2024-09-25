
# No hace falta constructor dado que la clase Padre tiene
# su propio constructor en el cual ya guarda el valor, y
# para acceder a este valor solo necesitamos usar self.
class TextoPersonalizado(str):

    # Con self accedemos al texto introducido por parametro
    def formato(self, separador):
        return separador.join(self.split())

    def splitlines(self, keepends = False):
        return self.split("\n")

    def imprimir(self):
        print(self)


texto = TextoPersonalizado("Hola buenas tardes")
texto.imprimir()
print(texto.formato(":"))


class NumeroPersonalizado(dict):

    def calculo(self, mi_numero):
        pass


class TextoPersonalizado(str):

    # Con self accedemos al texto introducido por parametro
    def formato(self, separador):
        return separador.join(self.split())

    def splitlines(self, keepends = False):
        pass


texto = TextoPersonalizado("Hola buenas tardes")
print(texto.formato(":"))

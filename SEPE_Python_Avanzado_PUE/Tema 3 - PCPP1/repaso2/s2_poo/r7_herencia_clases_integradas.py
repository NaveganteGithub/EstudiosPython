

class Textos(str):

    def empaquetar(self):
        return self.strip().split()

mi_texto = Textos("Hola buenas tardes")
print(mi_texto.empaquetar())

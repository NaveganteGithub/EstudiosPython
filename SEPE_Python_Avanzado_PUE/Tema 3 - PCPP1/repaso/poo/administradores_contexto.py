
class MiClase:

    def __init__(self, x):
        self.coordenada = x

    def __enter__(self):
        self.coordenada *= 5
        print(self.coordenada)
        return self.coordenada

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type, exc_val, exc_tb, sep=" :: ")
        return self.coordenada + 4

with MiClase(4) as entrada:
    print(entrada)

with MiClase(5) as entrada:
    print(entrada) # return
    print(entrada.coordenada / 0)


print(dir(entrada))
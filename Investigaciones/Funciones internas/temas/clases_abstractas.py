from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14 * self.radio ** 2

# Intentar crear una instancia de FiguraGeometrica generará un error
# porque es una clase abstracta.
# figura = FiguraGeometrica()

rectangulo = Rectangulo(base=5, altura=3)
print(f"Área del rectángulo: {rectangulo.calcular_area()}")

circulo = Circulo(radio=2)
print(f"Área del círculo: {circulo.calcular_area()}")

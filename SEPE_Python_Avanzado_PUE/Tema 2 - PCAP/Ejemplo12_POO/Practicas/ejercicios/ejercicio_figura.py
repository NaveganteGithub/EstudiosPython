import math

class Figura:

    def __init__(self, x, y):
        self.set_x(x)
        self.set_y(y)

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def calcular_area(self):
        pass

    def __str__(self):
        return "[{}, {}]".format(self.x, self.y)

class Circulo(Figura):

    def __init__(self, x, y, radio):
        self.radio = radio
        super().__init__(x, y)

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

    def __str__(self):
        return super().__str__() + f", {self.radio}"

class Triangulo(Figura):

    def __init__(self, x, y, base, altura):
        self.base = base
        self.altura = altura
        super().__init__(x, y)

    def calcular_area(self):
        return self.base * self.altura / 2
    
    def __str__(self):
        return super().__str__() + f"{self.base}, {self.altura}"

class Cuadrado(Figura):

    def __init__(self, x, y, lado):
        super().__init__(x, y)
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def __str__(self):
        return super().__str__() + f"{self.lado}"

figura = Figura(20, 6)
print(figura)
print(figura.calcular_area())

circulo = Circulo(20, 6, 50)
print(circulo)
print(round(circulo.calcular_area(), 2))

triangulo = Triangulo(20, 6, 40, 25)
print(triangulo.calcular_area())
print(triangulo)

cuadrado = Cuadrado(20, 6, 12)
print(cuadrado.calcular_area())
print(cuadrado)

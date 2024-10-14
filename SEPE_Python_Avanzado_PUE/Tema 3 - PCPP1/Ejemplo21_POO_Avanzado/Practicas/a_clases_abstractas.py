# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 12:33:16 2024

@author: Ismael Montoro Peñasco
"""

import abc
import math


class Figura(abc.ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Marcar el metodo como abstracto
    # @abc.abstractclassmethod # OBSOLETO
    @classmethod 
    @abc.abstractmethod
    def calcular_area(self):
        pass

    def __str__(self):
        return f"[{self.x},{self.y}]"   # [20, 6]

class Circulo(Figura):
    def __init__(self, x, y, radio):
        Figura.__init__(self,x, y)
        self.radio = radio

    def calcular_area(self):
        return math.pi *  math.pow(self.radio, 2)

    def __str__(self):
        return super().__str__() + f", Radio: {self.radio}"

class Triangulo(Figura):
    def __init__(self, x, y, base, altura):
        super().__init__(x, y)
        self.base = base
        self.altura = altura

    # def calcular_area(self):
    #     return self.base * self.altura / 2

    def __str__(self):
        return super().__str__() + f", Base: {self.base}, Altura: {self.altura}"

# Con @abc.abstractclassmethod # OBSOLETO
# TypeError: Can't instantiate abstract class Figura without an implementation for abstract method 'calcular_area'
# ''' Crear objetos y devolver el area y sus datos '''
"""figura = Figura(20,6)
print("Area de la figura:",figura.calcular_area())  # None
print(figura)
"""

circulo = Circulo(20,6, 50)
print("Area del circulo:", round(circulo.calcular_area(), 2) )
print(circulo)

# TypeError: Can't instantiate abstract class Triangulo without an implementation for abstract method 'calcular_area'
triangulo = Triangulo(20, 6, 40, 25)
print("Area del triangulo:", round(triangulo.calcular_area(), 2))
print(triangulo)

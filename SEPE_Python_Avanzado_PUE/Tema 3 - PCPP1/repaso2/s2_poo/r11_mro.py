"""
En Python tenemos la posibilidad de realizar herencia multiple ademas de la herencia simple. El MRO o Method Resolution
Orden es una caracteristica de python que permite elegir que metodo usar primero automaticamente.

Cuando se diseña un programa, una de las cosas mas importantes que podemos hacer es diseñar una arquitectura
jerarquica para la herencia de clases. Muchas veces cuando las diseñamos en un principio puede que sea solida
y eficiente, pero con el tiempo, cuando se van agregando mas clases, puede surgir un problema llamado el problema
del diamante.

El problema del diamante es una ambiguedad que puede surgir cuando se implementan las clases de tal manera que
A hereda a B y C, y B y C herederan a D.
"""

class A:

    def imprimir(self):
        print("Hola")

class B(A):

    def imprimir_clase_a(self):
        print("Hola B")

class C(A):

    def imprimir_clase_a(self):
        print("Hola C")

class D(B, C):

    def imprimir_clase_a_desde_d(self):
        print("Hola D")

clase = D()
clase.imprimir_clase_a()
clase.imprimir()
clase.imprimir_clase_a()
clase.imprimir_clase_a_desde_d()

"""class A:

    def __init__(self):
        self.n = 1

    @staticmethod
    def imprimir():
        print("Hola")

class B(A):

    def imprimir_clase_a_desde_b(self):
        print(self.n)

class C(A):

    def imprimir_clase_a_desde_c(self):
        print(self.n)

class D(B, C):

    def imprimir_clase_a_desde_d(self):
        print(self.n)

clase = D()
clase.imprimir_clase_a_desde_b()
clase.imprimir_clase_a_desde_c()
clase.imprimir()
clase.imprimir_clase_a_desde_d()"""
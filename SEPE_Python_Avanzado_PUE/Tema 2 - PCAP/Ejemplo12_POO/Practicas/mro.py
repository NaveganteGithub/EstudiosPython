'''En herencia multiple podemos invocar el constructor con el nombre de la clase,
esta es una manera explícita de llamar al constructor padre digamos,
viene bien ya que es más directa y tienes un control más preciso digamos.
super() es más dinámico y sigue el MRO (Method Resolution Order) para determinar
el método que se va a llamar, es decir maneja automáticamente el orden de resolución de métodos.

En los lenguajes de programación orientada a objetos, el problema del diamante es una ambigüedad
que surge cuando dos clases B y C heredan de A, y la clase D hereda de B y C. Si un método en D
llama a un método definido en A, ¿por qué clase lo hereda, B o C?
'''

'''
class A:

    def super_clase(self):
        print("Superclase")

class B(A):

    def medio(self):
        print("Clase en el medio")

class C(A, B):

    def abajo(self):
        print("Clase abajo")

class D(B, C):

    def muy_abajo(self):
        print("Clase muy abajo")

c = C()
# c.abajo() # TypeError: Cannot create a consistent method resolution
# c.medio() # TypeError: Cannot create a consistent method resolution order (MRO) for bases A, B
# c.super_clase() # TypeError: Cannot create a consistent method resolution order (MRO) for bases A, B
'''

class AA:

    def super_clase(self):
        print("Superclase")

class BB(AA):

    def medio(self):
        print("Clase BB en el medio")

class CC(AA):

    def medio(self):
        print("Clase CC en el medio")

class DD(BB, CC):
# class DD(CC, BB):
    def abajo(self):
        print("Clase abajo")

dd = DD()
dd.abajo()
dd.super_clase()
dd.medio()
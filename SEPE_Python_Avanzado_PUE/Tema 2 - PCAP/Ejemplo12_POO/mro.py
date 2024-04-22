"""
En herencia multiple podemos invocar el constructor con el nombre de la clase, 
esta es una manera explícita de llamar al constructor padre digamos, 
viene bien ya que es más directa y tienes un control más preciso digamos. 

super() es más dinámico y sigue el MRO (Method Resolution Order) 
para determinar el método que se va a llamar, es decir maneja 
automáticamente el orden de resolución de métodos.
"""

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

c = C()
#c.abajo() # TypeError: Cannot create a consistent method resolution

# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases A, B
#c.super_clase()
'''





# Problema del diamanate
class AA:
    def super_clase(self):
        print("Superclase")

class BB(AA):
    def medio(self):
        print("Clase BB en el medio")

    def super_clase(self):
        print("Superclase de BB")

class CC(AA):
    def medio(self):
        print("Clase CC en el medio")

    def super_clase(self):
        print("Superclase de CC")

class DD(CC, BB):
    # En Python como no se permite sobrecarga de metodos
    # Los metodos comunes entra CC y BB, se resuelve que al ser
    # BB la segunda clase en herencia busca los metodos heredados de CC
    def abajo(self):
        print("Clase abajo")

dd = DD()
dd.abajo()  # Clase abajo
dd.super_clase()  # Superclase

# llama al metodo de la clase BB porque con herencia multiple es la primera class DD(BB, CC):
dd.medio()  # Clase BB en el medio

# Si intercambio el orden saldra CC    Clase CC en el medio

'''
    MRO: Orden de ejecuccion de los metodos
    dd.abajo(): Busca ese metodo en la clase DD y lo encuentra
    dd.medio(): Empieza a buscar en la primera clase que pongo en herencia multiple DD(CC, BB)
                      ejecuta el de la clase CC
    dd.super_clase(): Este metodo esta de forma implicita en DD
'''

print(DD().__mro__)
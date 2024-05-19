"""
Polimorfismo del Griego Poli (Muchos) y Morfe (forma)

Es la capacidad de un objeto (en este caso una clase) 
de adoptar multiples formas.
"""

class Animal:

    def onomatopeya(self):
        return "Sonido de los animales"

class Perro(Animal):

    def __init__(self):
        super().__init__()
    def onomatopeya(self):
        return "Ladrar"

class Vaca(Animal):
    def onomatopeya(self):
        return "Muge"

class Caballo(Animal):

    def __init__(self):
        super().__init__()
    def onomatopeya(self):
        return "Relincha"

print(Animal().onomatopeya())
print(Perro().onomatopeya())
print(Vaca().onomatopeya())
print(Caballo().onomatopeya())
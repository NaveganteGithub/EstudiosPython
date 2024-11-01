
class Padre:

    def __init__(self, nomb, ed, inteli, fuer):
        self.nombre = nomb
        self.edad = ed
        self.inteligencia = inteli
        self.fuerza = fuer

    def informacion(self):
        return self.nombre, self.edad, self.inteligencia, self.fuerza

    def levanta_peso(self, peso):
        return self.fuerza > peso

    def resultado(self, problema):
        return self.inteligencia > problema

class Madre:

    def __init__(self, nomb, ed, compasiva):
        self.nombre = nomb
        self.edad = ed
        self.compasion = compasiva

    def perdon(self):
        return self.compasion

class Hijo(Padre, Madre):

    def __init__(self, nomb, ed, inteli, fuer, compasivo, espi):
        Padre.__init__(self, nomb, ed, inteli, fuer)
        Madre.__init__(self, nomb, ed, compasivo)
        self.espiritu = espi

    def informacion(self):
        return self.nombre, self.edad, self.espiritu

clase_padre = Padre("Daniel", 50, 25, 24)
clase_hijo = Hijo("Alex", 25, 30, 32, 25, 10)
print(clase_padre.levanta_peso(10))

print(clase_padre.informacion())
print(clase_hijo.informacion())

print(clase_padre.resultado(15))
print(clase_hijo.resultado(15))

print(clase_hijo.perdon())

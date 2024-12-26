
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

class Hijo(Padre):

    def __init__(self, nomb, ed, gen, inteli, fuer, espi):
        super().__init__(nomb, ed, gen, inteli, fuer)
        self.espiritu = espi

    # Sobreescritura de un método de la clase Padre.
    def informacion(self):
        return self.nombre, self.edad, self.espiritu

clase_padre = Padre("Daniel", 50, 25, 24)
clase_hijo = Hijo("Alex", 25, 30, 32, 10)
print(clase_padre.levanta_peso(10))

print(clase_padre.informacion())
print(clase_hijo.informacion())

print(clase_padre.resultado(15))
print(clase_hijo.resultado(15))
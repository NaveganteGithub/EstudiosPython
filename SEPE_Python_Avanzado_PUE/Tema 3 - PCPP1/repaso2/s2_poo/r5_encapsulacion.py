
class Persona:

    def __init__(self, nombre, edad, altura):
        self.nombre_persona = None
        self.edad_persona = None
        self.altura_persona = None

        self.mi_nombre = nombre
        self.mi_edad = edad
        self.altura_persona = altura

    @property
    def mi_nombre(self):
        return self.nombre_persona

    @mi_nombre.setter
    def mi_nombre(self, nuevo_nombre):
        self.nombre_persona = nuevo_nombre

    @mi_nombre.deleter
    def mi_nombre(self):
        del self.nombre_persona

    @property
    def mi_edad(self):
        return self.edad_persona

    @mi_edad.setter
    def mi_edad(self, nueva_edad):
        self.edad_persona = nueva_edad

    @mi_edad.deleter
    def mi_edad(self):
        del self.edad_persona

    @property
    def mi_altura(self):
        return self.altura_persona

    @mi_altura.setter
    def mi_altura(self, nueva_altura):
        self.altura_persona = nueva_altura

    @mi_altura.deleter
    def mi_altura(self):
        del self.altura_persona


clase = Persona("David", 25, 1.50)
print(clase.mi_nombre)
print(clase.mi_edad)
print(clase.mi_altura)

clase.mi_nombre = "Daniel"
clase.mi_edad = 14
clase.mi_altura = 1.75

print(clase.mi_nombre)
print(clase.mi_edad)
print(clase.mi_altura)

del clase.mi_nombre
del clase.mi_edad
del clase.mi_altura

print(clase.mi_nombre)
print(clase.mi_edad)
print(clase.mi_altura)

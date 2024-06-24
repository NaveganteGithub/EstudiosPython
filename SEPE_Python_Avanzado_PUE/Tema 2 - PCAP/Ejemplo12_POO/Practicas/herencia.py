class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        return f"{self.nombre}: {self.edad}"

class Empleado(Persona):

    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def mostrar_info(self):
        # return "{}, {}, {}".format(self.nombre, self.edad, self.sueldo)
        # return "{}, {}".format(super().mostrar_info(), self.sueldo)
        return f"{super().mostrar_info()}, {self.sueldo}"

p1 = Persona("Juan", 27)
print(p1.mostrar_info())

empleado_1 = Empleado("Juan", 27, 57000)
print(empleado_1.mostrar_info())

print(issubclass(Empleado, Persona))

print(Persona.__subclasses__())
print(Empleado.__subclasses__())
print(Persona.__subclasses__()[0].__name__)

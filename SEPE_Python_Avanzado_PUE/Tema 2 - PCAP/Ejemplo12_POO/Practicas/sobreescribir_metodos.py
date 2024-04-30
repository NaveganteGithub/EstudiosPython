class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        return f"{self.nombre}: {self.edad}"

    def __str__(self):
        return f"{self.nombre}: {self.edad} de str"

class Empleado(Persona):
    """
    Documentacion de la Clase Empleado
    """

    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def mostrar_info(self):
        # return "{}, {}, {}".format(self.nombre, self.edad, self.sueldo)
        # return "{}, {}".format(super().mostrar_info(), self.sueldo)
        return f"{super().mostrar_info()}, {self.sueldo}"

    def __str__(self):
        print(self.nombre)
        # print(self.__edad) # AttributeError: 'Empleado' object has no attribute '_Empleado__edad'
        # print(super().__edad) # AttributeError: 'super' object has no attribute '_Empleado__edad'
        # print(super()._Persona__edad) # AttributeError: 'super' object has no attribute '_Persona__edad'
        return f"{super().__str__()}, {self.sueldo}"

p1 = Persona("Juan", 27)
print(p1.mostrar_info())

empleado_1 = Empleado("Juan", 27, 57000)
print(empleado_1.mostrar_info())

print(issubclass(Empleado, Persona))

print(Empleado.__bases__)

print(Persona.__bases__)

print(dir(Persona))

print(p1)
print(p1.__str__())
print(p1.__hash__())
print(empleado_1.__str__())
print(empleado_1.__doc__)
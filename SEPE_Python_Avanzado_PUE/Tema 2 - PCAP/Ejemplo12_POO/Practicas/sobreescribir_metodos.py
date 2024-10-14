""" Si escribimos aqui sobreescribimos el atributo __doc__ de Python"""
import string as s, random as r

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

print("isinstance a Persona", isinstance(p1, Persona))
print("isinstance a Empleado", isinstance(p1, Empleado))

print(issubclass(Empleado, Persona))

# Me devuelve la clase padre o base, en caso de tener varias base 
# me listara todas las clases superiores. Palabra de referencia: HERENCIA
print("Atributo __bases__ de Empleado:", Empleado.__bases__)
print("Atributo __bases__ de Persona:", Persona.__bases__)
# __module__ sirve para comprobar a que modulo pertenene cada clase
# en caso de que salga __main__ como resultado. Palabra de referencia: MODULO
print("Atributo __module__ de Empleado:", Empleado.__module__)
print("Atributo __module__ de Persona:", Persona.__module__)
print("Atributo __module__ de Template:", s.Template.__module__)
print("Atributo __module__ de Random:", r.Random.__module__)
# __name__ me sirve para comprobar el nombre de la clase. Palabra de referencia: CLASE
plantilla = s.Template
numero = r.Random
print("Atributo __name__ de Template:", plantilla.__name__)
print("Atributo __name__ de Random:", numero.__name__)
print("Atributo __name__ de Empleado:", Empleado.__name__)
print("Atributo __name__ de Persona:", Persona.__name__)

print(dir(Persona))

print(p1)
print(p1.__str__())
print(p1.__hash__())
print(empleado_1.__str__()) # Ver el string de la clase
print(empleado_1.__doc__) # Ver la documentacion de la clase
print(__doc__)

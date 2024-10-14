class Fecha:

    def __init__(self, dia, mes, anyo):
        self.dia = dia
        self.mes = mes
        self.anyo = anyo

    def mostrarFecha(self):
        # print(self.dia, self.mes, self.anyo, sep="/")
        return f"{self.dia}/{self.mes}/{self.anyo}"

fecha = Fecha(20,5,2000)
print(fecha.mostrarFecha())
fecha = Fecha(20,87,-26)
fecha.dia = 1000
print(fecha.mostrarFecha())
print()

############

class Fecha_Encapsulada:

    def __init__(self, dia, mes, anyo):
        self.__dia = 0
        self.__mes = 0
        self.__año = 0
        self.set_dia(dia)
        self.set_mes(mes)
        self.set_año(anyo)

    def get_dia(self):
        return self.__dia

    def set_dia(self, dia):
        self.__dia = 1
        if dia in [n for n in range(1,31 + 1)]:
            self.__dia = dia
        else:
            print("Dia no es valido")

    def set_mes(self, mes):
        self.__mes = 1
        if mes in [n for n in range(1,12 + 1)]:
            self.__mes = mes
        else:
            print("Mes no es valido")

    def set_año(self, año):
        self.__año = 1
        if año in [n for n in range(2024,2025 + 1)]:
            self.__año = año
        else:
            print("Año no es valido")

    def mostrarFecha(self):
        # print(self.dia, self.mes, self.anyo, sep="/")
        return f"{self.__dia}/{self.__mes}/{self.__año}"

hoy = Fecha_Encapsulada(20,5,2024)
print(hoy.mostrarFecha())
hoy = Fecha_Encapsulada(20,87,-26)
hoy = Fecha_Encapsulada(20,5,2024)
print(hoy.mostrarFecha())
hoy.__dia = 1000 # ENCAPSULACION DEVIL
print(hoy.mostrarFecha())

# __ es el prefijo para atributos y metodos privados
# _ es el prefijo para atributos y metodos protegidos

print(hoy._Fecha_Encapsulada__dia) # name mangling -> Acceder a la variable privada o metodo privado
'''
In name mangling process any identifier with two leading 
underscore and one trailing underscore is textually 
replaced with _classname__identifier where classname is 
the name of the current class. 

It means that any identifier of the form __geek (at 
least two leading underscores or at most one trailing 
underscore) is replaced with _classname__geek, where 
classname is the current class name with leading 
underscore(s) stripped.

En el proceso de alteración de nombres, cualquier 
identificador con dos guiones bajos iniciales y uno 
final se reemplaza textualmente con _classname__identifier 
donde classname es el nombre de la clase actual.

Significa que cualquier identificador de la forma __geek 
(al menos dos guiones bajos iniciales o como máximo un 
guión bajo final) se reemplaza con _classname__geek, 
donde classname es el nombre de la clase actual sin 
los guiones bajos iniciales.
'''

print(hoy.__dict__)

"""En el mundo de la programación, la instrospección
es la habilidad para determinar el tipo de un objeto
en tiempo de ejecución.
"""
print(dir(hoy))
print(dir(Fecha_Encapsulada))
print(hasattr(hoy, "set_año"))
print(hasattr(hoy, "__mes"))
print(hasattr(hoy, "_Fecha_Encapsulada__mes"))

setattr(hoy, "__prueba", 5)
print(getattr(hoy, "__prueba"))

print(getattr(hoy, "set_año"))
print(Fecha_Encapsulada.__name__)
print(type(hoy).__name__)
print(type(Fecha_Encapsulada).__name__)
print(hash(hoy))

print(isinstance(hoy, Fecha_Encapsulada))
print(isinstance(hoy, (Fecha_Encapsulada, Fecha)))
print(isinstance(hoy, Fecha))

# print(getattr(hoy, __mes)) # NameError: name '__mes' is not defined
print(setattr(hoy, "_Fecha_Encapsulada__mes", 8))
print(getattr(hoy, "_Fecha_Encapsulada__mes"))
# Las Metaclases son objetos que nos permiten definir la estructura de una Clase

class MiClase:

    @staticmethod
    def imprimir():
        print("Hola")

clase = MiClase()
print(type(clase))  # <class '__main__.MiClase'>
print(type(MiClase))  # <class 'type'>

# PRIMERA FORMA

# Crear instancia de una clase llamada mi clase.
# type("Nombre de clase", ("Clases que va a heredar"), {"Atributo1": "Valor1", "Atributo2": "Valor2"})
mi_clase = type("Clase", (MiClase,), {"texto": "Hola", "numero": 65456})
print(mi_clase.texto)

# SEGUNDA FORMA

class Fruta:

    nombre: str
    cantidad: int

    def __init__(self, nomb, cant):
        Fruta.nombre = nomb
        Fruta.cantidad = cant

def saludar(nombre):
    return "Buenas tardes " + nombre

class Metaclase(type):

    def __new__(cls, name_class, base_class, attr_class):
        # Crear una instancia de clase con los atributos que nos pasen
        print("Antes", name_class)
        name_class = name_class + "Hola"
        print("Despues", name_class)

        print("Antes", base_class)
        base_class = list(base_class)
        base_class.append(Fruta)
        base_class = tuple(base_class)
        print("Despues", base_class)

        print("Antes", attr_class)
        attr_class['mi_atributo'] = 5
        attr_class['funcion'] = saludar
        attr_class['mi_clase'] = mi_clase
        print("Despues", attr_class)

        return type(name_class, base_class, attr_class)

class MiClase2(MiClase, metaclass=Metaclase):

    attri1: int
    attri2: int

    def __init__(self, n1, n2):
        MiClase.attri1 = n1
        MiClase.attri2 = n2

    @staticmethod
    def imprimir():
        print(MiClase2.attri1, MiClase2.attri2, MiClase2.__name__, MiClase2.__bases__)

clase = MiClase2(5, 2)
clase.imprimir()

print("Mi Clase", clase.mi_clase)
clase.mi_clase.imprimir()

print("Mi funcion", end=" ")
print(MiClase2.__dict__['funcion']("Ismael"))

print("Mi atributo", clase.mi_atributo)
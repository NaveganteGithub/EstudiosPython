# En Python las clases son en realidad objetos, las clases de
# Python son "clases" entre comillas

# Una clase define las caracteristicas de un objeto
# Una metaclase define las caracteristicas de una clase
class Producto:
    pass

produc=Producto()

print(type(produc)) # Instancia de la clase Producto

# Aqui podemos ver la metaclase type, Python no es como Java donde
# todas las clases descienden de Object, en cambio hay una metaclase
# que define las caracteristicas de las otras clases
print(type(Producto))

# Podemos definir clases otras clases usando type directamente y
# obtener una instancia, el primer parametro es el nombre de clase,
# el segundo es donde indicamos la herencia o las "bases" de clase,
# y el tercero son los atributos
mi_clase = type('Prueba', (), {'valor': 15})
print(mi_clase)  # <class '__main__.Prueba'>
print(type(mi_clase))  # <class 'type'>
print(mi_clase.valor)  # 15

# Ahora podemos crear clases con metodos donde estos seran atributo
def metodo(self): # Obligatorio el self, si no lo pones produce TypeError
    print("Hola")

mi_clase = type('Prueba2', (), {'mivalor': 15, "mimetodo": metodo})

mi_instancia = mi_clase()
mi_instancia.mimetodo()



class Metaclase(type):

    # __new__ sirve para indicar que se lleve a cabo
    # la construccion del objeto, se ejecuta antes
    # que __init__, este metodo sirve para ejecutar
    def __new__(cls, nombre_clase, superclases, atributos):
        print("Nombre", nombre_clase, "Clases superiores", superclases, "Atributos", atributos, sep="; ")
        # Al final del metodo devolveremos el contructor type para devolver la clase creada
        return type(nombre_clase, superclases, atributos)


# En el momento en el que se crea el objeto MiClase que en realidad
# es un objeto, por eso aunque no instanciemos la clase MiClase, si
# estamos creando el objeto MiClase que es una clase.
#
# Si no usaramos la metaclase "Metaclase" no imprimiria la informacion
#
# Nombre; MiClase; Clases superiores; (); Atributos; {'__module__': '__main__',
# '__qualname__': 'MiClase', '__annotations__': {'nombre': <class 'str'>, 'apellido': <class 'str'>},
# 'nombre': 'David', 'apellido': 'Montoya', 'imprimir': <function MiClase.imprimir at 0x000002AF0C57B9C0>}
#
# Puedes comprobarlo si ejecutas la declaracion
# de la Metaclase y la clase MiClase
class MiClase(metaclass=Metaclase):

    nombre: str = "David"
    apellido: str = "Montoya"

    def imprimir(self):
        print(self.nombre, self.apellido)


mi_instancia = MiClase()

mi_instancia.imprimir()



class Metaclase2(type):

    def __new__(cls, nombre_clase, superclases, atributos):

        diccionario={}
        for element, valor in atributos.items():
            diccionario[element] = valor

        diccionario["otroAtributo"] = "Hola"

        print(diccionario)

        return type(nombre_clase, superclases, diccionario)

class MiClase2(metaclass=Metaclase2):

    nombre: str = "David"
    apellido: str = "Montoya"

    def imprimir(self):
        print(self.nombre, self.apellido)

mi_instancia = MiClase2()

# https://www.youtube.com/watch?v=nQBAGph1eCM
# https://www.youtube.com/watch?v=4rarIb1Mhz4
# https://realpython.com/python-metaclasses/
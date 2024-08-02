
class Producto:

    def __init__(self, identificator, descripcion, precio):
        self.id = identificator
        self.descripcion = descripcion
        self.precio = precio

    # Cuando mostremos el objeto, mostrara la informacion y/o
    # los datos de la clase de manera legible o entendible para
    # el humano. Aqui esta la informacion INFORMAL.
    def __str__(self):
        return f"ID {self.id}, Descripcion: {self.descripcion}, Precio: {self.precio}"

    # Cuando el objeto se elimine y lo mostremos, que se muestre "Clase eliminada"
    def __del__(self):
        print("Clase eliminada: Producto; Identificador:", self.id)
        # print("Clase eliminada:", Producto.__name__, "; Identificador:", self.id)

    # Retorna un valor numerico, imprendiscible para comparar elementos del conjunto
    def __hash__(self):
        # return int(self.id + len(self.descripcion) + self.precio)

        suma = 0
        for letra in self.descripcion:
            suma += ord(letra)

        return int(self.id + suma + self.precio)

    # Cuando mostremos el objeto, mostrara la informacion y/o
    # los datos de la clase en formato mas crudo, como los valores
    # de clase en una tupla
    def __repr__(self):
        return f"{self.id}; {self.descripcion}; {self.precio}"

    # Podemos modificar el metodo format para que ciertas clases puedan
    # tener ciertos parametros que nosotros podemos especificar
    def __format__(self, format_spec):
        separador = ":"
        resultado = ""
        formatos = format_spec.split()
        for f in formatos:
            match f:
                case "%i":
                    resultado += str(self.id)
                case "%d":
                    resultado += str(self.descripcion)
                case "%p":
                    resultado += str(self.precio)
                case _:
                    raise ValueError("Valor de formato no reconocido")
            resultado += separador

        return resultado

    # Al sobreescribir __dir__ podemos especificar como
    # realizar la introspeccion de una instancia
    def __dir__(self):
        print("Sobreescrita")
        return Producto.__dict__

    # Con bool podemos modificar la funcion bool() y con ello podemos definir
    # si la instancia bajo ciertas condiciones que nosotros podemos especificar
    # tendra un valor True o False.
    def __bool__(self):
        es_entero = type(self.id) is int
        es_texto = type(self.descripcion) is str
        es_flotante = type(self.precio) is float
        return es_entero and es_texto and es_flotante


print("__str__")
p1 = Producto(1, "Pantalla", 129.50)
p2 = Producto(1, "Pantalla", 129.50)
p1bis = Producto(1, "Pantallo", 129.50)

print(p1)
# Antes de sobreescribir el metodo: <__main__.Producto object at 0x00000216326A7C90>
# Despues de sobreescribir el metodo: ID 1, Descripcion: Pantalla, Precio: 129.5

p3 = Producto(3, "Teclado", 37.95)
p4 = Producto(4, "Raton", 19.80)

print("__hash__")
# Antes de sobreescribir el metodo hash: Da una excepcion: TypeError: unhashable type: 'Producto'
# Despues de sobreescribir el metodo hash: p1 y p2 al tener el mismo id, entiende que son iguales
conjunto = {p1, p2, p3, p4, p1bis}
# print(*conjunto)
for p in conjunto:
    print(p)

print("__repr__")
# Antes de sobreescribir el metodo repr: <__main__.Producto object at 0x000001B961E034A0>
# Despues de sobreescribir el metodo repr: 1; Pantalla; 129.5
print(p2.__repr__())
print(repr(p2))

print("__format__")
print(p1.__format__("%i %d %p"))
print(format(p1, "%i %d %p"))

print("__dir__")
# Antes de sobreescribir el metodo __dir__: ['id', 'descripcion', 'precio', '__module__', '__init__', '__str__',
#                                           '__del__', '__hash__', '__repr__', '__format__', '__dict__', '__weakref__',
#                                           '__doc__', '__new__', '__getattribute__', '__setattr__', '__delattr__',
#                                           '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__reduce_ex__',
#                                           '__reduce__', '__getstate__', '__subclasshook__', '__init_subclass__',
#                                           '__sizeof__', '__dir__', '__class__']
# Despues de sobreescribir el metodo repr: {'__module__': '__main__',
#                                           '__init__': <function Producto.__init__ at 0x0000023672474CC0>,
#                                           '__str__': <function Producto.__str__ at 0x0000023672474E00>,
#                                           '__del__': <function Producto.__del__ at 0x0000023672474EA0>,
#                                           '__hash__': <function Producto.__hash__ at 0x0000023672474F40>,
#                                           '__repr__': <function Producto.__repr__ at 0x0000023672474FE0>,
#                                           '__format__': <function Producto.__format__ at 0x0000023672475080>,
#                                           '__dir__': <function Producto.__dir__ at 0x0000023672475120>,
#                                           '__dict__': <attribute '__dict__' of 'Producto' objects>,
#                                           '__weakref__': <attribute '__weakref__' of 'Producto' objects>,
#                                           '__doc__': None}
print(p1.__dir__())

print("__bool__")
print(bool(p1))
print(p1.__bool__())
p5 = Producto("5", "Raton", "19.80")
print(bool(p5))
print(p5.__bool__())

try:
    # Dos cosas a tener en cuenta cuando sobreescribamos __del__:
    # Primero al eliminar una instancia de una clase muy concreta con la
    # palabra reservada del, se eliminaran tambien las otras instancias
    # que sean de la misma clase.
    # Segundo el metodo __del__ no puede devuelver nada, por lo tanto, para
    # que puedas retornar datos tendras que usar print, logs o persistencia
    # en ficheros.
    print("__del__")
    print("Clase", p1)
    del p1
    print(p1)
except NameError:
    pass

print(p2)
print(p4)

# p1 = Producto(1, "Pantalla", 129.50)
p2 = Producto(1, "Pantalla", 129.50)
# p1bis = Producto(1, "Pantallo", 129.50)
# p3 = Producto(3, "Teclado", 37.95)
p4 = Producto(4, "Raton", 19.80)

print(p2)
print(p4)

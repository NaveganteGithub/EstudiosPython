m = 256
n = m
o = 256
print(id(m), id(n), id(o))

x = 257
y = x
z = 257
print(id(x), id(y), id(z))


class Producto:

    # contador = 0 # Variable publica y de clase
    __contador = 0  # Variable privada y de clase

    def __init__(self, descripcion, precio):
        self.descripcion = descripcion
        self.precio = precio
        Producto.__contador += 1

    def get_contador(self):
        return self.__contador

    def __str__(self):
        return f"ID: {Producto.__contador}, Descripcion: {self.descripcion}, Precio: {self.precio}"
    
p1 = Producto("Pantalla", 129.50)
print(p1.__hash__())
print(id(p1))
print(hex(id(p1)))
print(p1.__repr__())

import inspect
atributos_clase = inspect.getmembers(Producto, lambda a: not inspect.isroutine(a))
print ([a[0] for a in atributos_clase]) # ['_Producto__contador', '__class__', '__dict__', '__doc__', '__module__', '__weakref__']

atributos_instancia = vars(p1)
print(atributos_instancia.keys()) # dict_keys(['id', 'descripcion', 'precio']) 
class Producto:
    # Variables de clase: solo hay una copia en la clase
    #contador = 0  # publica
    __contador = 0  # privada

    '''
    def __init__(self, id, descripcion, precio):
        # Variables de instancia: cada objeto mantiene una copia de estas variables
        self.id = id
        self.descripcion = descripcion
        self.precio = precio
        # incrementar el contador
        Producto.contador += 1
        #contador += 1  # UnboundLocalError: local variable 'contador' referenced before assignment
        #self.contador += 1  NameError: name 'self' is not defined
    '''

    def __init__(self, descripcion, precio):
        # Variables de instancia: cada objeto mantiene una copia de estas variables
        # incrementar el contador
        Producto.__contador += 1
        self.id = Producto.__contador
        self.descripcion = descripcion
        self.precio = precio

    # Metodo de clase: solo hay una copia y reside en la clase
    # Quitamos como argumento el puntero self
    def getContador():
        return Producto.__contador

    def __str__(self):
        return f"ID: {self.id}, Descripcion: {self.descripcion}, Precio: {self.precio}"

'''
p1 = Producto(1, "Pantalla", 129.50)
print("Cuantos productos tengo?", p1.contador)
p2 = Producto(2, "Teclado", 58.95)
print("Cuantos productos tengo?", p2.contador)
'''

# Al ser el contador publico puedo cambiar su valor
# Producto.contador = 10
Producto.__contador = 1100   # crea esa variable de clase
print("********", Producto.__contador)
print(dir(Producto))


# Acceso a recursos de clase (estaticos):   Clase.recurso
#print("Contador:", Producto.__contador)
print("Contador:", Producto.getContador())

p1 = Producto("Pantalla", 129.50)
print("Contador:", Producto.getContador())
p2 = Producto("Teclado", 58.95)
print("Contador:", Producto.getContador())
p3 = Producto("Raton", 25)
print("Contador:", Producto.getContador())
print(p1)
print(p2)
print(p3)

print("ID 1:", hex(id(p1._Producto__contador)))  # Variable de clase
print("ID 2:", hex(id(p1.__contador)))
print("ID 3:", hex(id(p2.__contador)))
print("ID 4:", hex(id(Producto.__contador)))
print("ID 5:", hex(id(p2._Producto__contador)))
print("ID 6:", hex(id(Producto._Producto__contador)))

#print(hasattr(p1, "__contador"))
#print(hasattr(p1, "_Producto__contador"))
print(p2.__contador)
print(p3.__contador)


class A:
    # Los metodos estaticos pertenecen a la clase y no se heredan
    def hola():
        print("Hola")

    def adios(self):
        print("Adios")

class B(A):
    pass

b= B()
#b.hola() # TypeError: A.hola() takes 0 positional arguments but 1 was given
b.adios()



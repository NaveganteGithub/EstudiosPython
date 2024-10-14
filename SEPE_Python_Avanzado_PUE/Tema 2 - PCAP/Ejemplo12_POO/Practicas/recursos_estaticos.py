'''class Producto:

    contador = 0

    def __init__(self, id, descripcion, precio):
        self.id = id
        self.descripcion = descripcion
        self.precio = precio
        Producto.contador += 1

    def __str__(self):
        return f"ID: {self.id}, Descripcion: {self.descripcion}, Precio: {self.precio}"

p1 = Producto(1, "Pantalla", 129.50)
# print(p1.contador)
print(Producto.contador)
p2 = Producto(2, "Teclado", 58.95)
# print(p2.contador)
print(Producto.contador)

print(p1)
print(p2)


'''

class Producto:

    # contador = 0 # Variable publica y de clase
    __contador = 0  # Variable privada y de clase

    def __init__(self, descripcion, precio):
        self.descripcion = descripcion
        self.precio = precio
        Producto.__contador += 1

    def get_contador(self):
        return self.__contador
    
    def get_contador_estatico():
        return Producto.__contador

    def __str__(self):
        return f"ID: {Producto.__contador}, Descripcion: {self.descripcion}, Precio: {self.precio}"

# print(Producto.__contador) # Da error porque tiene el self y si convierte en un metodo de instancia
print(Producto.get_contador_estatico())

p1 = Producto("Pantalla", 129.50)
print(p1)
print(p1.get_contador())
p2 = Producto("Teclado", 58.95)
print(p2)
print(p1.get_contador())
p3 = Producto("Teclado", 58.95)
print(p3)
print(p1.get_contador())

print(hasattr(p1, "__contador"))
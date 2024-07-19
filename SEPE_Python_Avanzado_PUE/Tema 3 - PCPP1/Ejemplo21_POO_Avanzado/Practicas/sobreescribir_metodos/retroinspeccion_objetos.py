
class Producto:

    def __init__(self, identificator, descripcion, precio):
        self.id = identificator
        self.descripcion = descripcion
        self.precio = precio

    def __instancecheck__(self, instance):
        print("Sobreescrito")
        # return instance is self
        return instance is not self

    def __subclasscheck__(self, subclass):
        print("Sobreescrito, lista de subclases:", Producto.__subclasses__())
        return subclass is Producto.__subclasses__()
        # return subclass is not Producto.__subclasses__()


p1 = Producto(1, "Pantalla", 129.50)
print(p1.__instancecheck__(p1))
print(p1.__subclasscheck__(p1))

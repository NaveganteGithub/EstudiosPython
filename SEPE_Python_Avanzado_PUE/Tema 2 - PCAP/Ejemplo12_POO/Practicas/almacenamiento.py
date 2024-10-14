a = 254
b = a
c = 254
print(id(a), id(b), id(c)) # 140736112507224 140736112507224 140736112507224

m = 256
n = m
o = 256
print(id(m), id(n), id(o)) # 140736112507288 140736112507288 140736112507288

x = 257
y = x
z = 257
print(id(x), id(y), id(z)) # 2905006845712 2905006845712 2905006845712


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
print(p1.__hash__()) # 181563160211
print(id(p1)) # 2905010563376
print(hex(id(p1))) # 0x2a4601f6930
print(p1.__repr__()) # <__main__.Producto object at 0x000002A4601F6930>

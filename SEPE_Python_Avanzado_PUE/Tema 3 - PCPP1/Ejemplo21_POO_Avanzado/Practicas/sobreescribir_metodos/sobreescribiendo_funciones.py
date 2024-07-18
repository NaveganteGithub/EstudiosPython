
class Producto:

    def __init__(self, identificator, descripcion, precio):
        self.id = identificator
        self.descripcion = descripcion
        self.precio = precio

    def __str__(self):
        return f"ID {self.id}, Descripcion: {self.descripcion}, Precio: {self.precio}"

    def __abs__(self):
        print("Sobreescrito")
        return abs(self.precio)

    def __round__(self, n2=None):
        print("Sobreescrito")
        if self.precio is None:
            return 0
        return round(self.precio, n2)


p1 = Producto(1, "Pantalla", -129.55)
p2 = Producto(1, "Pantalla", 129.55)
p1bis = Producto(1, "Pantallo", 129.50645645678967896)
p3 = Producto(3, "Teclado", 37.95)
p4 = Producto(4, "Raton", 19.85)

print("Absolutos", abs(p1), "Valor anterior", p1)

print("Redondeo", round(p3, 1), "Valor anterior", p3)
print("Redondeo", round(p1bis, 5), "Valor anterior", p3)
print("Redondeo", round(20.2352155156156, 5))

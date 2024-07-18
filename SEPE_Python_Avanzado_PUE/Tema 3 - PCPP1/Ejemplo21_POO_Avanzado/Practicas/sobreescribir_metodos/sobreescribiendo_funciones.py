
class Producto:

    def __init__(self, identificator, descripcion, precio):
        self.id = identificator
        self.descripcion = descripcion
        self.precio = precio

    def __str__(self):
        return f"ID {self.id}, Descripcion: {self.descripcion}, Precio: {self.precio}"

    def __abs__(self):
        print("Sobreescrito")
        return self

    def __round__(self, n, n2=None):
        print("Sobreescrito")
        if n is None:
            return round(self.valor)
        return round(self.valor, n)


p1 = Producto(1, "Pantalla", -129.50)
p2 = Producto(1, "Pantalla", 129.50)
p1bis = Producto(1, "Pantallo", 129.50)
p3 = Producto(3, "Teclado", 37.95)
p4 = Producto(4, "Raton", 19.80)

print("Absolutos", abs(p1), "Valor anterior", p1)
print("Redondeo", round(p1, 1), "Valor anterior", p1)

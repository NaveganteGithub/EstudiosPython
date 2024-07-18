
class Producto:

    def __init__(self, identificator, descripcion, precio):
        self.id = identificator
        self.descripcion = descripcion
        self.precio = precio

    def __str__(self):
        return f"ID {self.id}, Descripcion: {self.descripcion}, Precio: {self.precio}"

    """Por el momento, parece ser que no funciona la
    sobreescritura en los operadores uninarios + y -
    """
    def __pos__(self):
        print("Sobreescrito")
        return +self.id

    def __neg__(self):
        print("Sobreescrito")
        return -self.id


p1 = Producto(1, "Pantalla", 129.50)
p2 = Producto(1, "Pantalla", 129.50)
p1bis = Producto(1, "Pantallo", 129.50)
p3 = Producto(3, "Teclado", 37.95)
p4 = Producto(4, "Raton", 19.80)

a = +p3
b = -p3
print("Positivo", a)
print("Negativo", b)
print("Positivo", p3.__pos__())
print("Negativo", p3.__neg__())

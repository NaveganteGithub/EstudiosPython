class Producto:

    def __init__(self, id, desc, precio):
        self.id = id
        self.desc = desc
        self.precio = precio

    def __str__(self):
        return f"{self.id}, {self.desc}, {self.precio}"

productos = list()
linea = open("productos.txt", "rt", encoding="utf-8")
products = linea.read()
for i in linea:
    id, descripcion, precio = products.split('|')
    print(id, descripcion, precio)
    producto = Producto(id, descripcion, precio)
    productos.append(producto)
linea.close()
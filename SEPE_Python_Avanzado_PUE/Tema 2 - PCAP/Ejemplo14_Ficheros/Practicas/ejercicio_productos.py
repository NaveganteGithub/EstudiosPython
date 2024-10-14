class Producto:

    def __init__(self, id, desc, precio):
        self.id = id
        self.desc = desc
        self.precio = precio

    def __str__(self):
        return f"{self.id}, {self.desc}, {self.precio}"

productos = list()

listado = open("productos.txt", "rt", encoding="utf-8")
products = listado.read().split("\n")
for i in range(len(products)):
    products[i] = products[i].split("|")
    for i2 in range(len(products[i])):
        if i2 == 1:
            products[i][i2] = products[i][i2].strip().title()
        elif i2 == 2:
            products[i][i2] = "{:.2f}".format(float(products[i][i2].strip()))
        else:
            products[i][i2] = int(products[i][i2].strip())

listado.close()

for pro in products:
    producto_actual = Producto(pro[0], pro[1], pro[2])
    productos.append(producto_actual)

# print(products)
print(productos)

for pro_list in productos:
    print(pro_list)
'''
    crear una lista de objetos de tipo producto
    el id debe ser numerico entero
    la descripcion debe tener solo la primera letra mayuscula
    el precio ha de ser numerico real
'''
class Producto:
    def __init__(self, id, descripcion, precio):
        self.id = id
        self.descripion = descripcion
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Descripcion: {self.descripion}, Precio: {self.precio}"
'''
eso se denomina “Context Manager
with open("productos.txt", "wt", encoding="utf-8") as fichero:
    fichero.write("Hola")
'''

fichero = open("productos.txt", "rt", encoding="utf-8")
lineas = fichero.readlines()

lista_productos = []
for linea in lineas:
    datos = linea.split("|")
    # cogemos el primer dato, le quitamos los espacios en blanco y lo convertimos en entero
    id = int(datos[0])
    descripcion = datos[1].strip().title()
    precio = float(datos[2].rstrip("\n"))
    lista_productos.append(Producto(id, descripcion, precio))

fichero.close()

for prod in lista_productos:
    print(prod)
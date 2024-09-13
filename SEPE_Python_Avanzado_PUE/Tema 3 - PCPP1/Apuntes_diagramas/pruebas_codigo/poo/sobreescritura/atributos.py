
# Es curioso si utilizamos Pycharm para sobreescribir estos metodos
# solo tendra en cuenta los atributos de clase y no los de instancia
# lo digo porque me ha pasado que en Python al intentar pedir con el
# metodo getattr podia acceder a las variables de instancia, sin embargo
# lo ejecuto con PyCharm y el metodo getattr no me detecta las variables
# de instancia pero si las de clase

class Atributos:

    producto: str
    precio: float

    def __init__(self, producto, precio):
        Atributos.producto = producto
        Atributos.precio = precio

    def __getattr__(self, item):
        return f"El atributo {item} no existe"

    def __getattribute__(self, item):
        valor = super().__getattribute__(item)
        return item, valor

    def __setattr__(self, item, data):
        exec(f"Atributos.{item} = {data}")

    def __delattr__(self, item):
        exec(f"del Atributos.{item}")
        print("Atributo eliminado")


mi_atributo = Atributos("Manzana", 2.10)

print(getattr(mi_atributo, "producto"))
print(getattr(mi_atributo, "id"))
setattr(mi_atributo, "precio", 5.20)
print(getattr(mi_atributo, "precio"))
delattr(mi_atributo, "producto")

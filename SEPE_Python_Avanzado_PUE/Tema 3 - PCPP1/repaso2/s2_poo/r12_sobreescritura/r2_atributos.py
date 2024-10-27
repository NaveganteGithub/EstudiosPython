
class Atributos:

    def __init__(self, nombre, edad):
        self.mi_nombre = nombre
        self.mi_edad = edad

    def __getattribute__(self, item):
        print(f"Has pedido {item}")
        valor = super().__getattribute__(item)
        return valor

    def __getattr__(self, item):
        return f"{item} no existe"

    def __setattr__(self, clave, valor):
        print(f"{clave} a cambiado su valor a {valor}")
        super().__setattr__(clave, valor)

    def __delattr__(self, item):
        valor = super().__getattribute__(item)
        super().__delattr__(item)
        print(f"{item} tenia el valor {valor}")

clase = Atributos("Alejandro", 52)
print(getattr(clase, "mi_nombre"))
print(getattr(clase, "mi_nomb"))

setattr(clase, "mi_nombre", "Lorena")
print(getattr(clase, "mi_nombre"))

delattr(clase, "mi_nombre")

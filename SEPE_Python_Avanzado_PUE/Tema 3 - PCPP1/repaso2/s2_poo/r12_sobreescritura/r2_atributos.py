
class Atributos:

    def __init__(self, nombre, edad):
        self.mi_nombre = nombre
        self.mi_edad = edad

    # getattr tiene dos posibilidades, que encuentre o
    # no encuentre el atributo a procesar

    # en caso de encontrar el atributo procesará esta logica
    def __getattribute__(self, item):
        print(f"Has pedido {item}")
        valor = super().__getattribute__(item)
        return valor

    # en caso de no encontrar el atributo procesará esta logica
    def __getattr__(self, item):
        return f"{item} no existe"

    # Modifica el comportamiento del método setattr
    def __setattr__(self, clave, valor):
        print(f"{clave} a cambiado su valor a {valor}")
        super().__setattr__(clave, valor)

    # Modifica el comportamiento del método delattr
    def __delattr__(self, item):
        valor = super().__getattribute__(item)
        super().__delattr__(item)
        print(f"{item} tenia el valor {valor}")


# El constructor como tiene inserciones a variables
# de instancia el método setattr se activara
clase = Atributos("Alejandro", 52)
print("-" * 20)

print(getattr(clase, "mi_nombre"))
print("-" * 20)

print(getattr(clase, "mi_nomb"))
print("-" * 20)

setattr(clase, "mi_nombre", "Lorena")
print(getattr(clase, "mi_nombre"))
print("-" * 20)

delattr(clase, "mi_nombre")
print("-" * 20)

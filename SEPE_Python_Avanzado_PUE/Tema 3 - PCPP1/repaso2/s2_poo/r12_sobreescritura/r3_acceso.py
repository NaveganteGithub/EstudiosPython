import random


class Acceso:

    def __init__(self, nombre, edad):
        self.mi_nombre = nombre
        self.mi_edad = edad
        self.codigo = list(str(random.randint(1000, 10000)))

    def __getitem__(self, item):
        print(f"{item} a sido pedido")
        return exec(f"self.{item}")

    def __setitem__(self, clave, valor):
        print(f"{clave} a cambiado su valor {valor}")
        if type(valor) is str:
            exec(f"self.{clave} = '{valor}'")
        else:
            exec(f"self.{clave} = {valor}")

    def __delitem__(self, clave):
        print(f"Borrando {clave}")
        exec(f"del self.{clave}")

    def __len__(self):
        return len(self.mi_nombre)

    def __iter__(self):
        return iter(self.codigo)

    def __contains__(self, item):
        print(f"Analizando {item}")
        return item in self.mi_nombre

clase = Acceso("Daniel", 21)
print(clase["mi_nombre"])

clase["mi_nombre"] = "David"
print(clase["mi_nombre"])

print(len(clase))

print("a" in clase)

for l in clase:
    print(l, end="")

print()

del clase["mi_nombre"]

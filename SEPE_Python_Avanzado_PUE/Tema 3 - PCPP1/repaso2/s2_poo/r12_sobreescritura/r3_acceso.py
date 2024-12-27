
class Acceso:

    def __init__(self, nombre, edad):
        self.mi_nombre = nombre
        self.mi_edad = edad

    # getitem permite modificar el modo de acceder a las variables
    def __getitem__(self, item):
        print(f"{item} a sido pedido")
        return exec(f"self.{item}")

    # setitem permite modificar el comportamiento de las inserciones
    def __setitem__(self, clave, valor):
        print(f"{clave} a cambiado su valor {valor}")
        if type(valor) is str:
            exec(f"self.{clave} = '{valor}'")
        else:
            exec(f"self.{clave} = {valor}")

    # delitem permite modificar el comportamiento de la palabra reservada del
    def __delitem__(self, clave):
        print(f"Borrando {clave}")
        exec(f"del self.{clave}")

    # Permite modificar el comportamiento de la función len
    def __len__(self):
        return len(self.mi_nombre)

    # Permite realizar iteradores personalizados
    # para cada instancia de clase
    def __iter__(self):
        return iter(list(self.mi_nombre))

    # Permite modificar comportamiento de la palabra reservada "in"
    # ante las instancias de la clase
    def __contains__(self, item):
        print(f"Analizando {item}")
        return item in self.mi_nombre

clase = Acceso("Daniel", 21)
print("-" * 20)

print(clase["mi_nombre"])
print("-" * 20)

clase["mi_nombre"] = "David"
print("-" * 20)

print(clase["mi_nombre"])
print("-" * 20)

print(len(clase))
print("-" * 20)

print("a" in clase)
print("-" * 20)

for l in clase:
    print(l, end=".")

print()
print("-" * 20)

del clase["mi_nombre"]

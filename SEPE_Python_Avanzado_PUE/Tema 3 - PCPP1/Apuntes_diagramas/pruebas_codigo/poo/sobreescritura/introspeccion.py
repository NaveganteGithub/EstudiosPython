
class Introspeccion:

    def __init__(self, producto: str, precio: float) -> None:
        self.producto = producto
        self.precio = precio

    def __str__(self):
        return f"{self.producto} cuesta {self.precio} euros."

    def __del__(self):
        print("Producto eliminado")

    def __hash__(self) -> int:
        identificador = len(self.producto) ** 7
        identificador *= self.precio
        return int(identificador)

    def __repr__(self) -> str:
        return f"{self.producto}; {self.precio}"

    def __dir__(self):
        return self.__dict__

    def __bool__(self) -> bool:
        return self.precio > 0

    def __format__(self, format_spec: str):
        cadena = format_spec.replace("%name", self.producto)
        cadena = cadena.replace("%price", str(self.precio))
        return cadena


mi_clase = Introspeccion("Manzana", 0.20)
print(mi_clase)
print(hash(mi_clase))
print(repr(mi_clase))
print(dir(mi_clase))
print(format(mi_clase, "%name %price"))

mi_clase_2 = Introspeccion("Platano", 0.00)
print(bool(mi_clase))
print(bool(mi_clase_2))

del mi_clase_2

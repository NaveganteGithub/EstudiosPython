
class MiClase:

    coordenadas: list

    def __init__(self, x, y, z):
        MiClase.coordenadas = [x, y, z]

    def __getattr__(self, item):
        return "No existe " + item

    def __getattribute__(self, item):
        return super().__getattribute__(item)

    # Es mejor utilizar las variables de clase para sobreescritura y no self, para evitar errores de recursividad
    def __setattr__(self, key, value):
        return exec(f"MiClase.{key} = {value}")

    def __delattr__(self, item):
        exec(f"del MiClase.{item}")
        print("Se ha eliminado", item)

clase = MiClase(5, 7, 12)
print(getattr(clase, "coordenadas"))
setattr(clase, "coordenadas", [2, 4, 2])
print(getattr(clase, "coordenadas"))
delattr(clase, "coordenadas")
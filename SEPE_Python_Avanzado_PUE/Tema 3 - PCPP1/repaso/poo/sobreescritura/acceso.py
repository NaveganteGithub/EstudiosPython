
class MiClase:

    def __init__(self, x, y, z):
        self.coordenadas = [x, y, z]

    def __len__(self):
        return self.coordenadas.__len__()

    def __iter__(self):
        return iter(self.coordenadas)

    def __contains__(self, item):
        return item in self.coordenadas

    def __getitem__(self, item):
        return self.coordenadas * 2

    def __setitem__(self, key, value):
        exec(f"{self}.{key} = {value * 2}")

    def __delitem__(self, key):
        exec(f"del self.{key}")
        print("Eliminado", key)

clase = MiClase(5, 7, 12)

for i in clase:
    print(i)

print(5 in clase)

print(len(clase))

print(clase.coordenadas)
clase.coordenadas = [2, 4, 2]
print(clase.coordenadas)
del clase.coordenadas

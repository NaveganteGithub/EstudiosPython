
class MiClase:

    def __init__(self, x, y, z):
        self.coordenadas = [x, y, z]

    def __str__(self):
        return f"Horizontal {self.coordenadas[0]} Vertical {self.coordenadas[1]} Profundidad {self.coordenadas[2]}"

    def __repr__(self):
        return f"{self.coordenadas[0]};{self.coordenadas[1]};{self.coordenadas[2]}"

    def __hash__(self):
        return sum(self.coordenadas)

    def __del__(self):
        print("Adios a " + self.__class__.__name__)
        del self

    def __dir__(self):
        return dir(MiClase)

    def __bool__(self):
        es_numero = False

        for c in self.coordenadas:
            es_numero = str(c).isdigit()
            if not es_numero:
                break

        return es_numero

    def __format__(self, format_spec: str):

        opciones = {"coorX": self.coordenadas[0], "coorY": self.coordenadas[1], "coorZ": self.coordenadas[2]}
        texto = format_spec.replace("coorX", str(opciones["coorX"]))

        for key, value in opciones.items():
            texto = texto.replace(key, str(value))

        return texto


clase = MiClase(5, 7, 12)

print(repr(clase))
print(hash(clase))
print(dir(clase))
print(bool(clase))
print(format(clase, "Hori: coorX; Verti: coorY; Profu: coorZ"))
del clase
print(clase)

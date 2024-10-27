
class Introspeccion:

    verdad: bool

    def __init__(self, nombre, edad):
        self.mi_nombre = nombre
        self.mi_edad = edad

    def __str__(self):
        return f"El nombre de esta clase es {self.mi_nombre}"

    def __del__(self):
        print(f"Eliminando {self.mi_nombre}")
        del self

    def __hash__(self):
        return self.mi_edad**22 + 45654231

    def __repr__(self):
        return "self.mi_nombre; self.mi_edad"

    def __dir__(self):
        return dir(Introspeccion)

    def __bool__(self):
        es_texto = type(self.mi_nombre)
        es_numero = type(self.mi_edad)
        return es_texto is str and es_numero is int

    def __format__(self, formato: str):
        nuevo_texto = ""
        for clave in formato:
            nuevo_texto = self.mi_nombre.replace(clave.lower(), clave.upper(), -1)

        return nuevo_texto



clase = Introspeccion("Lucia", 48)

print(clase)
print(hash(clase))
print(repr(clase))

print(dir(clase))
print(bool(clase))
print(format(clase, "ai"))

del clase
print(clase)


numeros = [1, 7, 8, 9, 6, 11, 2]


class Iterador:

    def __init__(self, iterador: list[int]):
        self.iterador = iterador

    def __iter__(self) -> iter:
        # Preprocesamiento antes de la iteración
        resultado = map(lambda n: n * 2, self.iterador)
        # Devolver iterador
        return iter(resultado)


mi_iterable = Iterador(numeros)

print("Iterador")
for num in mi_iterable:  # Iterar
    print(num)


class Longitud_Elevado_2:

    def __init__(self, objeto):
        self.mi_objeto = objeto

    # Dentro del len utilizamos for como contador
    # porque si lo hacemos con la propia funcion
    # len activaremos la recursividad y dará error
    def __len__(self):
        longitud = 0
        for _ in self.mi_objeto:
            longitud += 1
        return longitud * 2


mi_longitud = Longitud_Elevado_2(numeros)

print("Logitud ^2", len(mi_longitud), sep=" - ")


class Contenido:

    def __init__(self, contenido):
        self.contenido = contenido

    # Sin embargo este "in" no causa recursion, porque no estamos llamando
    # a una funcion de manera recursiva sino a un operador
    def __contains__(self, dato):
        return dato in self.contenido


mi_contenido = Contenido(numeros)

print(5 in mi_contenido)
print(7 in mi_contenido)


class Accesos:

    nombre: str
    edad: int

    def __init__(self, nomb, edad):
        Accesos.nombre = nomb
        Accesos.edad = edad
        self.id = 2

    def __getitem__(self, item):
        print("getitem")
        valores = Accesos.__dict__
        return valores[item]

    def __setitem__(self, key, value):

        print(Accesos.__dict__.keys())
        if key not in list(Accesos.__dict__.keys()):
            raise AttributeError

        print(key, value)
        exec(f"Accesos.{key} = '{value}'")

    def __delitem__(self, key):

        print(f"Eliminando {key}")
        print(Accesos.__dict__.keys())
        if key not in Accesos.__dict__.keys():
            raise AttributeError

        exec(f"del Accesos.{key}")


mi_acceso = Accesos("Daniel", 19)

print(mi_acceso['nombre'])

mi_acceso['nombre'] = "Adan"

print(mi_acceso['nombre'])

del mi_acceso['nombre']

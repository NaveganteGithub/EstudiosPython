from paprika import equals_and_hashcode, to_string, singleton, data

@equals_and_hashcode
@to_string
@singleton
class MiClase:

    dia: int
    mes: int
    tiempo: int


clase = MiClase(5, 4, 2012)
clase2 = MiClase(5, 4, 2013)
print(clase)
print(str(clase))
print(clase.dia)
print(clase == clase2)
print(hash(clase))

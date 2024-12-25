from paprika import singleton, to_string, data, equals_and_hashcode

# La libreria paprika nos permite reducir el código repetitivo hasta cierto punto.

"""@singleton
@to_string
@equals_and_hashcode"""
@data
class Datos:

    dia: int
    mes: int
    tiempo: int

clase = Datos(15, 4, 2024)
print(clase) # Datos@[dia=15, mes=4, tiempo=2024]

clase_2 = Datos(18, 9, 2024)
clase_3 = Datos(15, 4, 2024)
print(clase == clase_2) # True
print(clase == clase_3) # True

print(hash(clase)) # 2607810613518054557

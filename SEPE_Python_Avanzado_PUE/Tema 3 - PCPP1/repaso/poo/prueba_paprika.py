from paprika import singleton, equals_and_hashcode, to_string

# Si nombras tu programa de la misma manera que un modulo de python
# existente en tu proyecto, surge un error de importacion circular.
#
# Salida:
# ImportError: cannot import name 'data' from partially initialized module
# 'paprika' (most likely due to a circular import)
# (...EstudiosPython\SEPE_Python_Avanzado_PUE\Tema 3 - PCPP1\repaso\poo\prueba_paprika.py)
#
# Es un ImportError de tipo Importacion Circular, sale cuando intentas importar
# un modulo de python con el mismo nombre que el modulo que se esta programando

@equals_and_hashcode
@to_string
@singleton
class MiClase:

    dia: int
    mes: int
    tiempo: int


clase = MiClase(5, 6, 7)
clase2 = MiClase(5, 6, 7)
print(clase.dia)
print(clase)
print(clase == clase2)
print(hash(clase))

"""
5
MiClase@[dia=5, mes=6, tiempo=7]
True
-1350146935415579984
"""
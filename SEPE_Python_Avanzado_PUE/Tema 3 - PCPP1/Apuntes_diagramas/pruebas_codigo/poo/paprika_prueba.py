from paprika import to_string
# from paprika import equals_and_hashcode
# from paprika import singleton

@to_string
# @equals_and_hashcode
# @singleton
class Pruebas:

    prueba_biologica: bool
    daños: int
    informe: str


mis_pruebas = Pruebas()
mis_pruebas_2 = Pruebas()

# @to_string
print(mis_pruebas)
# Pruebas@[daños=7, informe=Los resultados del experimento son un exito, pero hemos perdido a
# todo nuestro personal, prueba_biologica=True]

# @equals_and_hashcode
print(mis_pruebas)  # <__main__.Pruebas object at 0x000001CEC537ACC0>
print(mis_pruebas == mis_pruebas_2)  # True

# @singleton
"""mis_pruebas_3 = Pruebas(True, 7, "Los resultados del experimento son un exito, se ha perdido a todo nuestro personal")
mis_pruebas_4 = Pruebas(False, 1, "Se realizaran mas pruebas")
print(mis_pruebas_3)
print(mis_pruebas_4)"""

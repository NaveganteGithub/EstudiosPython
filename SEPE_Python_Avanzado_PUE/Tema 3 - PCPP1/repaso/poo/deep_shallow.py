import copy

class MiClase:

    def __init__(self, c):
        self.coord = c

clase1 = MiClase(5)
clase2 = MiClase(444)

lista = [1, 2, 3, 4, clase1 , [1, 4, 6]]

lista_asignada = lista

print(id(lista_asignada))
print(id(lista))


copia_superficial_1 = list(lista)
copia_superficial_1[1] = 5
copia_superficial_1[5][1] = 15
copia_superficial_1[4] = clase2
print(lista, copia_superficial_1, sep="\n")

copia_superficial_2 = [o for o in lista]
copia_superficial_3 = lista.copy()
copia_superficial_4 = copy.copy(lista)

print(copia_superficial_2, copia_superficial_3, copia_superficial_4, sep="\n")

copia_profunda = copy.deepcopy(lista)

copia_profunda[1] = 75
copia_profunda[5][1] = 125
copia_profunda[4] = clase2

print(lista, copia_profunda, sep="\n")

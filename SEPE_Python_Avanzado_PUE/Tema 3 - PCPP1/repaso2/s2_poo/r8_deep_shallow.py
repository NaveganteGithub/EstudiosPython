import copy

# Asignar de direcciones de memoria
lista = [1,5,9,7,8,9,2,3,6,5,8,963,4]
copia = lista

print(lista, copia)
lista.append("111111111")
print(lista, copia)
print()

# Shallow Copy

lista = [1,5,9,7,8,9,2,3,6,5,8,963,4]

copia_1 = list(lista)
copia_2 = [i for i in lista]
copia_3 = lista.copy()

copia_4 = copy.copy(lista)

print(lista, copia_1, copia_2, copia_3, copia_4, sep="\n")
lista.append("111111111")
print(lista, copia_1, copia_2, copia_3, copia_4, sep="\n")
print()

# Deep Copy

lista = [1,5,[9,7,8,9],2,[3,6,5,8],963,4]
copia_superficial = copy.copy(lista)
copia_profunda = copy.deepcopy(lista)

print(lista, copia_superficial, copia_profunda, sep="\n")
lista.append("111111111")
lista[2].append("2222222222")
print(lista, copia_superficial, copia_profunda, sep="\n")

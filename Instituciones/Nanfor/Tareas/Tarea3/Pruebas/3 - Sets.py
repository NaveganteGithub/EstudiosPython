conjuntos = set()

print(conjuntos)

conjuntos = set([1,2,3,4,5])

print(conjuntos)

lista = [1,1,1,2,2,3,3,3,3,3,3,4,4,5,5,5,5,5,5,5,5,5,5,5,5] # No hace falta que se una lista tambien puede ser una tupla

conjuntos = set(lista)

print(conjuntos)

conjuntos.add(8)
print(conjuntos)

print(len(conjuntos))

print(2 in conjuntos)
print(7 in conjuntos)

conjuntos.remove(5)
print(conjuntos)

conjuntos.clear()
print(conjuntos)
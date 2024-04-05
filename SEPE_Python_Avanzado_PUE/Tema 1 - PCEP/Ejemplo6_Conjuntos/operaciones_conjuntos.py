numeros1 = {1,2,3,4,5,6,7,8,9}
numeros2 = {0,2,4,6,8,10}

# interseccion de conjuntos: elementos comunes en ambos
print(numeros1.intersection(numeros2))
print(numeros1 & numeros2)

# diferencia de conjuntos: elementos de un conjunto que no estan en el otro
print(numeros1.difference(numeros2))
print(numeros1 - numeros2)

# el orden es importante
print(numeros2.difference(numeros1))
print(numeros2 - numeros1)

# diferencia simetrica de conjuntos: la union de conjuntos menos los comunes
print(numeros1.symmetric_difference(numeros2))
print(numeros1 ^ numeros2)
# el orden no importa
print(numeros2.symmetric_difference(numeros1))
print(numeros2 ^ numeros1)

# union de conjuntos
print(numeros2.union(numeros1))
print(numeros1 | numeros2)

# modificar diferencia: borrar los elementos de un conjunto que estan en el otro
numeros1.difference_update(numeros2)
numeros1 -= numeros2
print(numeros1)  # en numero1 elimina los pares
print(numeros2)  # se mantiene intacto

'''
Te dejas:

set1.update(set2)
cjto.discard(elto)
set1.issuperset
set1.issubset
'''



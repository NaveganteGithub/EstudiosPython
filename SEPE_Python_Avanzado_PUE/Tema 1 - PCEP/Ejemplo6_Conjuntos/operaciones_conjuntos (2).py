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

# modificar diferencia: borrar los elementos de un conjunto que estan en el otro
numeros1.difference_update(numeros2)
numeros1 -= numeros2
print(numeros1)  # en numero1 elimina los pares
print(numeros2)  # se mantiene intacto

# union de conjuntos
print(numeros2.union(numeros1))
print(numeros1 | numeros2)

# update: Modifica el conjunto uniendo los elementos de otro conjunto
#numeros1.update(numeros2)
numeros1 |= numeros2
print(sorted(numeros1))  # en numero1 almacena numeros1 + numeros2
print(sorted(numeros1, reverse=True))
print(numeros2)  # se mantiene intacto

# discard: Borrar el elemento pasado como argumento si lo encuentra, sino no hace nada
numeros1.discard(2)
print(numeros1)

# si no encuentra el elemento con remove devuelve un error
# numeros1.remove(27) # KeyError: 27

# issuperset: comprueba si el primer conjunto contiene todos los datos del segundo 
print(numeros1.issuperset(numeros2))

nums1 = {1,2,3,4,5}
nums2 = {1,5}
print(nums1.issuperset(nums2))

# issubset: comprueba si el primer conjunto es subconjunto del segundo. 
# que todos los elementos del primer conjunto estan en el segundo
print(numeros1.issubset(numeros2))
print(nums2.issubset(nums1))


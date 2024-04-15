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

# Modifica los elementos de un conjunto agregando los elementos de otro conjunto
numeros1.update(numeros2)
print(numeros1)
numeros2.update(numeros1)
print(numeros2)

# Hace lo mismo que la funcion remove, con la diferencia de que si no encuentra el elemento no hace nada
numeros1.discard(2)
print(numeros1)
numeros2.discard(3)
print(numeros2)

# Ordena los elementos de la estructura
print(sorted(numeros1))
print(sorted(numeros2))
print(sorted(numeros1, reverse=True))
print(sorted(numeros2, reverse=True))

num1 = {2,5,6,8,7,9,10}
num2 = {2,5,6,8}

# Permite saber si el primer conjunto contiene todos los elementos del segundo
print(num1.issuperset(num2))
print(num2.issuperset(num1))

# Permite saber si el conjunto del parametro contiene todos los elementos del conjunto que utiliza la funcion
print(num1.issubset(num2))
print(num2.issubset(num1))
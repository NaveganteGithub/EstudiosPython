import copy

print("Asignamiento")
# Vamos a empezar con algo muy basico, cuando nosotros realizamos esta accion,
# no estamos copiando una lista, estamos asignando la direccion de memoria de
# una lista a otra variable.
lista = [1,2,3,4,5,6,7]
lista2 = lista
print(id(lista), id(lista2), sep=" --- ")

# Si cambiamos un valor de la lista2 cambia tambien de lista1 porque son la misma lista
lista2[0] = 5
print(lista, lista2, sep=" --- ")


print("Shallow Copy")
# Esto es un Shallow copy (Copia superficial), esto lo conocemos del PCEP, es cuando copiamos
# un objeto en python con sus datos, pero solamente para lista principal, porque en la nueva
# lista que se genere, esta contendra los datos primitivos, y las direcciones de memoria a las
# sublistas.
# Aqui lo estamos haciendo Shadow Copy usando un constructor.
lista = [4,1,2, [2,3], [4,5]]
lista2 = list(lista)
print(id(lista), id(lista2), sep=" --- ")
print(lista, lista2, sep=" --- ")

lista2[0] = 5
lista2[3][0] = 15
print(lista, lista2, sep=" --- ")

# Podemos realizar Shallow Copy de varias maneras
lista = [4,1,2, [2,3], [4,5]]
lista2 = [i for i in lista]
lista3 = lista.copy()
lista4 = copy.copy(lista)
print(lista, lista2, lista3, lista4, sep=" --- ")


print("Deep Copy")
# Deep Copy (o Copia Profunda) aqui copiamos todos los datos primitivos
# y todos los objetos que haya dentro de la lista, ya no tenemos el
# problema de las direcciones de memoria.
lista = [5,2,2, [2,3], [4,5]]
lista2 = copy.deepcopy(lista)
print(lista, lista2, sep=" --- ")

lista2[0] = 5
lista2[3][0] = 15
print(lista, lista2, sep=" --- ")


# Ahora podemos hacer deepcopy con objetos

class Pony:

    def __init__(self, n):
        self.name = n

poni_salvaje = Pony("Wild")
poni_salvaje2 = copy.copy(poni_salvaje)
print(id(poni_salvaje), id(poni_salvaje2), sep=" --- ")

ponis = [poni_salvaje, poni_salvaje2]
shallow_copy = copy.copy(ponis)
print(id(ponis[0]), id(shallow_copy[0]), sep=" --- ")

deep_copy = copy.deepcopy(ponis)
print(id(ponis[0]), id(deep_copy[0]), sep=" --- ")

# https://www.youtube.com/watch?v=Ezbitv-1paU
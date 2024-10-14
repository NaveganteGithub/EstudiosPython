# crear una lista con las vocales
# ulizando compresion, crear el diccionario donde:
#       - la clave es el indice de la lista
#       - el valor es la letra

lista = ["a", 'e', 'i', 'o', 'u']  # los strings pueden ir entre comillas dobles o simples
resultado = {}
for indice in range(len(lista)):
    resultado.update({indice:lista[indice]})
print(resultado)

# compresion:
resultado = {indice:lista[indice] for indice in range(len(lista)) }
print(resultado)


# la funcion enumerate retorna el indice y el elemento de ese indice
lista = ["a", 'e', 'i', 'o', 'u']  # los strings pueden ir entre comillas dobles o simples
resultado = {}
for clave, valor in enumerate(lista):
    resultado.update({clave:valor})
print(resultado)

resultado = {clave:valor for clave, valor in enumerate(lista)}
print(resultado)


# obtener un diccionario a partir de utilizar la funcion zip:
#       - una lista con lenguajes de programacion
#       - una lista con las versiones

lenguajes = ['Python', 'Java', 'PHP']
versiones = [3.10, 17, 8]
resultado = {}
for lenguaje, version in zip(lenguajes, versiones) :
    resultado.update({lenguaje:version})
print(resultado)

resultado = {lenguaje:version for lenguaje, version in zip(lenguajes, versiones)}
print(resultado)

diccionario_lenguajes = dict(zip(lenguajes,versiones))
print(diccionario_lenguajes)
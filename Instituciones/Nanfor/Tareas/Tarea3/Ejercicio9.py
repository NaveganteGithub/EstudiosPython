lista_numeros = [0,1,2,3,4,5,6,7,8,9]
lista_minusculas = list()
lista_mayusculas = list()
lista_simbolos = list()

for id in range(65, 90 + 1):
    lista_mayusculas.append(chr(id))
    lista_minusculas.append(chr(id + 32))

for id in range(32, 47 + 1), range(58, 64 + 1), range(91, 96 + 1), range(123, 126 + 1):
    for simbolo in id:
        lista_simbolos.append(chr(simbolo))
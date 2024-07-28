matriz = [[0] * 3 for _ in range(3)]

datos = {'a': [1, 2], 'b': [3, 4]}
diccionario_anidado = {clave: [valor * 2 for valor in valores] for clave, valores in datos.items()}

print(matriz)
print(datos)
print(diccionario_anidado)
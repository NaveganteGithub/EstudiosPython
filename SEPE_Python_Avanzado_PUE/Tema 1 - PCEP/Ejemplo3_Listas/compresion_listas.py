# Ejemplo 1
lista_palabras = ['casa', 'mesa', 'manzana', 'pijama']
longitud_palabras = []

for palabra in lista_palabras:
    longitud_palabras.append(len(palabra))
    
print("Longitud de palabras:",longitud_palabras)

''' compresion de lista'''
longitud_palabras = [len(palabra) for palabra in lista_palabras]
print("Longitud de palabras:",longitud_palabras)


# Ejemplo 2
num_pares = [num for num in range(0,12) if num % 2 == 0]
print("Numeros pares:", num_pares)

''' codigo '''
num_pares = []

for num in range(0,12) :
    if num % 2 == 0 :
        num_pares.append(num)
print("Numeros pares:", num_pares)


# Ejemplo 3
# Dado ese vector crear una lista solo los numeros impares 
vector = [[1,2,3], [4,5,6], [7,8,9]]

num_impares = []
for fila in vector :
    for num in fila :
        if num % 2 != 0 :
            num_impares.append(num)
print(num_impares)

num_impares = [num for fila in vector for num in fila if num % 2 != 0 ]
print(num_impares)

# Intentar devolver la lista de 2 dimensiones: [[1, 3] [5], [7,9]]
matriz_impares = []
for fila in vector :
    fila_impares = []
    for num in fila :
        if num % 2 != 0 :
            fila_impares.append(num)
    matriz_impares.append(fila_impares)
print(matriz_impares)

matriz_impares = [ [num for num in fila if num % 2 != 0] for fila in vector ]
print(matriz_impares)


# Ejemplo 4
# Con esta matriz devolver una lista con 2 filas: [[1,3,5,7], [2,4,6,8]]
matriz = [[1,2], [3,4], [5,6], [7,8]]

nueva_matriz = []
for i in range(len(matriz[0])):  # 0 y 1
    nueva_fila = []
    for fila in matriz :
        nueva_fila.append(fila[i])
    nueva_matriz.append(nueva_fila)
print(nueva_matriz)

nueva_matriz = [ [fila[i] for fila in matriz] for i in range(len(matriz[0]))]
print(nueva_matriz)

filas = [[row[0] for row in matriz], [row[1] for row in matriz]]
print(filas)
# lista de una dimension
lista = [1,2,3,4,5]  # un solo indice -> un bucle para recorrer
for num in lista :
    print(num,  end="  ")

# lista de 2 dimensiones
matriz = [ [2,7,4], [8,1,6], [3,9,5] ]  # 2 indices (fila, columna) -> 2 bucles

'''
2   7   4
8   1   6
3   9   5
'''

for fila in matriz :
    for num in fila :
        print(num,  end="  ")
    print()
    
# suma de la diagonal   2 + 1 + 5
# matriz = [ [2,7,4], [8,1,6], [3,9,5] ]
suma = 0
for fila in range(len(matriz)) :   # 0, 1, 2   len(matriz)-> 3 filas
    for col in range(len(matriz[fila])) :  # 0, 1, 2  len(matriz[fila]) -> 3 columnas
        if fila == col :
            suma += matriz[fila][col]
print("Suma de la diagonal:", suma)

# lista de 2 dimensiones no cuadradadas, cada fila tiene diferente numero de columnas
matriz = [ [2,7,4,1], [8,1], [3,9,5,6,0] ]  # 2 indices (fila, columna) -> 2 bucles
for fila in matriz :
    for num in fila :
        print(num,  end="  ")
    print()
    

# lista de 3 dimensiones -> cubo de rubbik
cubo = [ [ [0,1],[2,3],[4,5] ],      [[6,7],[8,9],[10,11]] ]   # 3 indices y 3 bucles
for x in cubo :
    for y in x :
        for z in y:
            print(z,  end="  ")
        print()
    print()
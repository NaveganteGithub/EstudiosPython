def generador_fibonacci(num):
    '''termino_1 = 0
    termino_2 = 1'''
    termino_1, termino_2 = 0, 1
    yield termino_1
    yield termino_2

    for n in range(num):
        suma = termino_1 + termino_2
        '''termino_1 = termino_2
        termino_2 = suma'''
        termino_1, termino_2 = termino_2, suma
        yield suma


for item in generador_fibonacci(10):
    print(item, end=" ") # 0 1 1 2 3 5 8 13 21 34 55 89
print()

print(list(generador_fibonacci(10))) # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(*generador_fibonacci(10), end=" ") # 0 1 1 2 3 5 8 13 21 34 55 89

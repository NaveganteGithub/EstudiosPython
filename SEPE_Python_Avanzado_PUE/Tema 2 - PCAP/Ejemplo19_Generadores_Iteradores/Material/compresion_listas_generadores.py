lista = [1 if x % 2 == 0 else 0 for x in range(10)]   # con corchetes
tupla = tuple(1 if x % 2 == 0 else 0 for x in range(10))
generador = (1 if x % 2 == 0 else 0 for x in range(10))  # con parentesis

print(lista) # [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
print(tupla) # (1, 0, 1, 0, 1, 0, 1, 0, 1, 0)
print(generador)  # <generator object <genexpr> at 0x1025c9a10>


# Las listas son iterables
for num in lista:
    print(num, end=" ")  # 1 0 1 0 1 0 1 0 1 0
print()

for num in generador:
    print(num, end=" ")  # 1 0 1 0 1 0 1 0 1 0
print()
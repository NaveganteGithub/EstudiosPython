def serie_numeros(num): # retorna Generator[int]
    for n in range(num):
        # return n   # TypeError: 'int' object is not iterable
        yield n # hace que sea un generador

for item in serie_numeros(10):
    print(item, end=" ")
print()

# generador para crear las primeras potencias de 2 hasta el numero indicado
# eje:  num 4 -> 1, 2, 4, 8  (2 elevado a 0,1,2,3)
def generador_potencias(num):
    for n in range(num):
        yield 2 ** n

for item in generador_potencias(4):
    print(item, end=" ")
print()
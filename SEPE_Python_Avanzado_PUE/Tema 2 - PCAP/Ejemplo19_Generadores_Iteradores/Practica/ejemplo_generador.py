def serie_numeros(num):
    for n in range(num):
        # return n # TypeError: 'int' object is not iterable
        yield n # Es como un return, pero para crear iteradores

for item in serie_numeros(10):
    print(item)

print()

# Generador para crear las primeras potencias de 2 hasta el numero indicado
# eje: num 4 -> 1, 2, 4, 8 (2 elevado a 0,1,2,3)

def potencias_num(ciclos: int):
    for p in range(ciclos):
        yield 2 ** p

for n in potencias_num(4):
    print(n)
print()

# fibonacci

def fibonacci(num: int):
    inicio = [0, 1]
    for n in range(num):
        if n == 0:
            yield 0
        elif n == 1:
            yield 1
        else:
            suma = inicio[0] + inicio[1]
            inicio[0] = inicio[1]
            inicio[1] = suma
            yield suma

for i in fibonacci(20):
    print(i)

print(list(fibonacci(20)))
print(*fibonacci(20), end=" ")

def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2

t = [x for x in powers_of_2(5)]
print(t)

the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
the_tuple = tuple(1 if x % 2 == 0 else 0 for x in range(10))
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))

print(the_list)
print(the_tuple)
print(the_generator)

for num in the_list:
    print(num, end=" ")

print()

for num in the_generator:
    print(num, end=" ")

print()
import random

# modulo.recurso

# Para generar numeros aleatorios entre 0 y 1, pero sin llegar a 1
print(random.random())
print(random.random())
print(random.random())

# Para generar numeros aleatorios cambiando la semilla
random.seed()  # sin semilla, coge por defecto la hora local
print("Sin semilla:",random.random())
random.seed(3)
print(random.random())
random.seed(3)
print(random.random())  # si la semilla es la misma, el valor es igual

for _ in range(4):
    random.seed(10)
    print(random.random())

random.seed(10)
for _ in range(4):
    print(random.random())

random.seed()
# randrange el ultimo valor no esta incluido
print("Numero entero entre 0 y 50:",random.randrange(50))
print("Numero entero entre 10 y 50;",random.randrange(10,50))
print("Numero entero entre 10 y 50 solo pares:",random.randrange(10, 50, 2)) # Inicio, Final, Salto

# randint si que lo incluye
print("Numeros 20 al 30:",random.randint(20,30)) # coge el valor 30 tambien
# randint no tiene step
#print("Numeros 20 al 30 solo pares:",random.randint(20,30, 2))

# Quiero obtener 5 numeros aleatorios
for i in range(5):
    print("Numero aleatorio:",random.randint(20,30))

''' Importante: los metodos randrange y randint pueden devolver numeros repetidos '''

# Generar numeros aleatorios sin duplicados
# choice: retorna un elemento aleatorio de la secuencia pasada como argumento lista o tupla
print("Choice:", random.choice([1,2,3,4,5,6]))
print("Choice:", random.choice((1,2,3,4,5,6)))

# sample: retorna el numero de elementos especificados aleatorios en una lista
# de la secuencia pasada como argumento lista o tupla
print("Sample:", random.sample([1,2,3,4,5,6], 2))
print("Sample:", random.sample([1,2,3,4,5,6], 3))
print("Sample:", random.sample((1,2,3,4,5,6), 1))
print("Sample:", random.sample((1,2,3,4,5,6), 2))

print("Sample:", random.sample(range(10), 2))
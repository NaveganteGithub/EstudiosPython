# Bucles

# While

'''
Bucle while es un estructura repetitiva
que lo que hara es repetir las
instrucciones de una parte del
codigo, mientras la condicional sea
verdadera
'''
my_condition = 0

'''
Este while se ejecuta eternamente,
porque la condicion siempre sera
verdadera

while my_condition < 10:
    print(my_condition)
'''

'''
Se ejecutara de dos en dos hasta
el final del bucle
'''
while my_condition < 10:
    print(my_condition)
    my_condition += 2

'''
A la final esto es como copiar un if con sus instrucciones
varias veces, aunque claro hacer un if varias veces no es
buena idea, es por ello que tenemos estructuras repetitivas
'''

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2

print("La ejecucion continua")

print()

'''
En los bucles while podemos realizar else para
que cuando terminen hagan algo que nosotros
queramos
'''
my_condition = 0

while my_condition < 10: # Este es como un if que se repite
    print(my_condition)
    my_condition += 2
else: # Este else pertenece al while
    print("Mi condicion es mayor o igual que 10")

print("La ejecucion continua")

print()

'''
Hacer esta estructura es lo mismo que hacer un while
y un if por separado
'''
my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
if my_condition == 10:
    print("Mi condicion es igual a 10")
else: # Este no pertenece al while
    print("Mi condicion es mayor o igual que 10")

print("La ejecucion continua")


my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2


if my_condition == 10:
    print("Mi condicion es igual a 10")
else: # Este no pertenece al while
    print("Mi condicion es mayor o igual que 10")

print("La ejecucion continua")

print()

'''
elif no esta permitido en para el bucle while, pero si else

my_condition = 10

while my_condition < 10:
    print(my_condition)
    my_condition += 2
elif my_condition == 10:
    print("Por favor, introduce un numero menor que 10")
else:
    print("Mi condicion es mayor o igual que 10")

print("La ejecucion continua")
'''

my_condition = 0

while my_condition < 20:
    my_condition += 2
    if my_condition == 15:
        print("Mi condicion es 15")
    
    print("Mi condicion es menor que 20")

print("La ejecucion continua")

print()

my_condition = 0

while my_condition < 20:
    my_condition += 5
    if my_condition == 15:
        print("Mi condicion es 15")
    
    print("Mi condicion es menor que 20")

print("La ejecucion continua")

print()

my_condition = 0

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condicion es 15")
    
    print("Mi condicion es menor que 20")

print("La ejecucion continua")

print()

'''
En los bucles while podemos encontrarnos con condiciones simples
pero tambien con condiciones complejas, por consecuencia tendremos
una condicion que pida que pare el bucle, para ello tenemos el break

En el ejemplo siguiente podemos ver como un bucle se ejecuta hasta
llegar a 15, para despues finalizar
'''
my_condition = 0

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detine la ejecucion")
        break # Detiene completamente el bucle
    
    print(my_condition)

print("La ejecucion continua")

print()

# For

'''
Un bucle nos sirve para iterar un listado de elementos, debera
cumplir con una condicional, la diferencia entre un for y un
while es que for va iterar tantas veces como elementos haya en
un objeto o cuantas veces indiquemos, mientras que while solo
cuando la condicion sea verdadera, cuando un for acceda a un
elemento ejecutara el codigo que tiene dentro
'''

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list: # Recorre la lista
    print(element)
    
print()

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")

for element in my_tuple: # Recorre la tupla
    print(element)
    
print()

my_set = {"Brais", "Moure", 35}

for element in my_set: # Recorre el set
    print(element)

print()

my_dict = {
            "Nombre":"Brais",
            "Apellido":"Moure",
            "Edad":35,
            1:"Python"
            }

'''
Reccorre el diccionario, accediendo a
los nombres de las claves
'''
for element in my_dict:
    print(element)
    
print()

my_dict = {
            "Nombre":"Brais",
            "Apellido":"Moure",
            "Edad":35,
            1:"Python"
            }

'''
Reccorre el diccionario, accediendo a
los valores de las claves
'''
for element in my_dict.values():
    print(element)
    

print()

my_dict = {
            "Nombre":"Brais",
            "Apellido":"Moure",
            "Edad":35,
            1:"Python"
            }

'''
Lista todos los valores del diccionario,
para meterlos a una lista, rematando con
la iteración del bucle for
'''
for element in list(my_dict.values()):
    print(element)
    
print()

for element in list(my_dict.values()):
    print(element)
else: # Podemos utilizar else para los bucles for
    print("El bucle for para diccionario ha finalizado")
    
print()

for element in my_dict:
    print(element)
    if element == "Edad":
        break # Podemos utilizar break en los for
else: # El else no ha sido ejecutado debido al break
    print("El bucle for para diccionario ha finalizado")
    
print()

for element in my_dict:
    print(element)
    if element == "Edad":
        break
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")
    
    
print()

for element in my_dict:
    print(element)
    if element == "Edad":
        break
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")
    
print("La ejecucion continua")

print()

'''
Podemos utilizar continue para los bucles, este nos sirve para decir
que termine con un ciclo de bucle y pase al siguiente
'''
for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")
    
print("La ejecucion continua")

print()

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    else:
        print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")
    
print("La ejecucion continua")

print()

'''
No utilices demasiado el continue, pues puede generar
codigo espagueti

Codigo espagueti: pues basicamente es un codigo, que se
ejecutara en varias lineas de forma no ordenada, en la programacion
un codigo se ejecuta de arriba hacia abajo, pero en el codigo
espagueti no, esto es un problema pues en caso de que surga
sera muy dificil la lectura del codigo para su mantenimiento
'''
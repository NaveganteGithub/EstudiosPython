# tuplas: colecciones ordenadas (con indice) pero inmutables
# si se permiten elementos duplicados
# se crean ()
# Ejemplos de uso: meses del año, dias de la semana, estados civil, puntos cardinales

# crear una tupla con los dias de la semana
dias = ('lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo')

# mostrar la tupla por pantalla
print(dias)

# mostrar el tipo
print(type(dias))   # <class 'tuple'>

# crear una tupla vacia
tupla_vacia = ()
tupla_vacia = tuple()

# recorrer una tupla
for dia in dias :
    print(dia, end=" ")
print()

for i in range(len(dias)):
    print(dias[i], end=" ")
print()

# Mostrar el miercoles
print("Miercoles:", dias[2])   # al indice siempre se accede con corchetes


'''  errores '''
#del dias[0]  # TypeError: 'tuple' object doesn't support item deletion
#dias[0] = 'otro sabado' # TypeError: 'tuple' object does not support item assignment
#dias.append('otro domingo')  # AttributeError: 'tuple' object has no attribute 'append'

# Cuantos elementos hay en la tupla (longitud)
print("Longitud:", len(dias))

# Como puede haber elementos repetidos, contar cuantos lunes hay
print("Cuantos lunes?", dias.count('lunes'))

# En que posicion esta el viernes
print(dias.index('viernes'))
print(dias.index('viernes', 2))  # busca a partir del indice 2

# Cancatenar tuplas
# TypeError: can only concatenate tuple (not "str") to tuple
#otra_tupla = dias + ('otro sabado')

# TypeError: can only concatenate tuple (not "int") to tuple
#otra_tupla = dias + (1)

# Para poder concatenar tuplas ha de tener varios elementos o forzar al interprete para que  lo vea como tupla
#otra_tupla = dias + (1,)
otra_tupla = dias + (1,2,3,4,5)
print(otra_tupla)

#otra_tupla = dias + ('otro sabado')  # Error es que no lo considera una tupla
otra_tupla = dias + ('otro sabado', "otro domingo") # si son varios elementos si los interpreta como tupla
print(otra_tupla)

# El orden es importante
otra_tupla = ('otro sabado',) + dias # Agremos la coma, ahora si lo interpreta como tupla
print(otra_tupla)

# TypeError: can only concatenate tuple (not "list") to tuple
#otra_tupla = dias + ['otro sabado', "otro domingo"]
otra_tupla = dias + tuple(['otro sabado', "otro domingo"])  # solo se pueden concatenar tuplas con tuplas
print(otra_tupla)

prueba = tuple([1])
prueba = tuple((1,))
print(prueba)

# tuplas de 2 dimensiones
tupla_2d = ( ('Juan', 27, 'Soltero'), ('Maria',), ('Luis', 43, 'Casado', '2 hijos') )
for empleado in tupla_2d :
    for dato in empleado :
        print(dato, end=" ")
    print()

''' slices  [begin:stop:step] '''  
# mostrar los datos de martes a jueves
print(dias[1:4])

# mostrar los dias de la semana al reves
print(dias[::-1])

''' operadores de pertenencia in y not in  '''
print('jueves' in dias)
print('jueves' not in dias)

# Convertir una tupla en lista
lista_dias = list(dias)
print(lista_dias)

lista_numeros = list( (1,2,3,4,5) )
print(lista_numeros)

lista_numeros = list( tuple((1,2,3,4,5)))
lista_numeros = list( tuple([1,2,3,4,5]))
print(lista_numeros)

# Otra forma de crear tuplas
lista_numeros = 1,2,3,4,5
print(lista_numeros)


# Ejemplo de compresion de tuplas
numeros = [1, 2, 3, 4, 5]
tupla_cuadrados = tuple((num, num ** 2) for num in numeros)
print(tupla_cuadrados)

# Creamos una tupla de tuplas con compresion
tupla_tuplas = tuple((x,y) for x in [0.4, 1.5, 5] for y in [-1.2, 0.2, -2.4] if x>y)
print(tupla_tuplas)
print(type(tupla_tuplas))

# Creamos una lista de tuplas con compresion
lista_tuplas = [(x,y) for x in [0.4, 1.5, 5] for y in [-1.2, 0.2, -2.4] if x>y]
print(lista_tuplas)
print(type(lista_tuplas))

# Desarrollo del ultimo ejemplo
lista_tuplas = []
for x in [0.4, 1.5, 5] :
    for y in [-1.2, 0.2, -2.4] :
        if x>y :
            lista_tuplas.append( (x,y) )
print(lista_tuplas)

# mostrar los metodos de la clase tuple
#print(dir(tuple))

# multiplicar listas
resultado = [1,2,3] * 2
print("Multiplicar listas", resultado)   # [1, 2, 3, 1, 2, 3]

# multiplicar tuplas
resultado = (1,2,3) * 2
print("Multiplicar tuplas", resultado)   # (1, 2, 3, 1, 2, 3)

mi_tupla = (1,2,3)
resultado = mi_tupla * -2
print("Multiplicar tuplas", resultado)   # ()
print("mi_tupla", mi_tupla)   # (1,2,3)

''' Funcion zip fusiona colecciones primero con primero, segundo con segundo'''
tupla1 = ('a','b')
tupla2 = (1,2)

tuplas = list(zip(tupla1, tupla2))
tuplas = zip(tupla1, tupla2)
for item in tuplas :
    print("-------",item)

# La funcion zip siempre devuelve tuplas.
# los argumentos pueden ser de diferentes tipos siempre que sean interables
lista1 = ['a','b']
lista2 = [1,2]
print(tuple(zip(lista1, lista2)))
print(list(zip(lista1, lista2)))

# si en una coleccion hay mas elementos que en la otra los ignora
print(list(zip(('a','b','c'), [1,2])))

for letra in "hola":
    print(letra)

print(tuple("hola"))

print(tuple(zip("lista1", "lista2")))

''' Funciones min, max y sum  '''
numeros = (1,2,3,4,5)
print("Min:",min(numeros))
print("Max:",max(numeros))
print("Sum:",sum(numeros))

print(sorted(numeros))
print(sorted(numeros, reverse=True))
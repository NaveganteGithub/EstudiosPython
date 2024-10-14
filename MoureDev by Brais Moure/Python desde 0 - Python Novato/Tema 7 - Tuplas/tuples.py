# Tuplas

'''
Una Tupla es una estructura inmutable, aqui
se debe de poner valores que sabemos que no
van a cambiar, pues en una tupla se deniega
el cambio o modificacion de cualquier dato.

No tienen muchas opciones, debido a que no
se pueden modificar de ninguna manera
    
    ¿Se puede eliminar datos de una tupla? NO
    ¿Se puede agregar datos a una tupla? NO
    ¿Se puede ordenar datos de una tupla? NO
    ¿Se puede modificar datos a una tupla? NO
    ¿Se puede leer los datos de una tupla? SI

Para crear una tupla se tiene que emplear la
funcion tuple() o ()
'''

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
my_other_tuple = (35, 60, 30)

# Acceder a tupla
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) # Fuera de rango
# print(my_tuple[-6]) # Fuera de rango

print(my_tuple.count("Brais")) # Nos dice cuantas veces se repite el elemento
print(my_tuple.index("Moure")) # Nos dice en que posicion esta el elemento por su indice
print(my_tuple.index("Brais"))

'''
No se pueden modificar datos

my_tuple[1] = 1.80
print(my_tuple)
'''

# Se pueden concatenar tuplas, puesto que creamos una nueva tupla
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

'''
Se pueden hacer subtuplas de las tuplas,
puesto que creamos una nueva tupla
'''
print(my_sum_tuple[3:6])

# Conversiones
'''
Para convertir una tupla en una lista hay
que aplicar el operador list() pasando por
paramentro la tupla a convertir
'''
my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "MoureDev"
my_tuple.insert(1, "Azul")

'''
Para convertir una lista en una tupla hay
que aplicar el operador tuple() pasando por
paramentro la tupla a convertir
'''
print(tuple(my_tuple))

my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

'''
Los datos cuanto mas inmutables sean mejor, puesto
que estaran mas seguros, si llegara el caso de que
necesites realizar modificaciones a la estructura,
pues cambias el tipo de estructura de tupla a lista
para hacer las modificaciones necesarias, para por
ultimo realizar el cambio de lista a tupla, pero eso
si, intenta hacer que tu programa tenga los datos
en una tupla de principio a fin para que sea todo
lo seguro que puedes en la ejecucion de tu programa.
'''

'''
Elimina completamente la tupla, no solo los datos,
ademas no confundas el eliminar los datos con eliminar
una estructura completa
'''
# del my_tuple[0] # Da error, ya que es inmutable
del my_tuple 
'''
Da error, pues la tupla ya no existe no esta definida
NameError: name 'my_tuple' is not define
'''
# print(my_tuple)
'''
Para hacer que tu programa sea mas eficiente procura que
tu estructura cuando pase a otro tipo, procura borrar la
estructuta anterior con del o con sobre escritura
'''
# Conviertes la estructura, pero eliminando la estructuta anterior que copiamos anteriormente
my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "MoureDev" # Trabajas con la estructura
my_tuple.insert(1, "Azul")

'''
Cuando termines de trabajar con la estructura,
eliminas la estructura con la que has
trabajado y dejas la nueva
'''
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))
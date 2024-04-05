# Sets

'''
Un set es un estructura desordenada, que no
admite repetidos, no indexada, que no permite
los datos redundantes, con una muy rapida velocidad
de ejecucion

Para crear un set se tiene que emplear la
funcion set() o {}, pero cuando se crea un
set con {} inicialmente creara un diccionario
pues {} se utiliza para crear diccionarios
hasta que se añaden nuevos datos directamente,
entonces ahi se convierte en un set, si
declara son la el operador set directamente
te crea un set vacio
'''

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario


my_other_set = {"Brais", "Moure", 35}
print(type(my_other_set)) # pero cuando agregas datos se convierte en un set

# Funciones

print(len(my_other_set)) # Contar elementos

'''
Esto da error, pues no se puede acceder de esta manera,
porque no esta indexado, ni menos ordenado
'''
# print(my_other_set[0])

'''
Un set es un estructura desordenada

Si te fijas el resultado te lo
muestra de forma diferente a
como lo escribes en el codigo

Este orden se debe a que para ordenarlos
se utiliza un algotitmo para ordenarlos
de forma aleatoria
'''
my_other_set.add("MoureDev") # Sirve para insertar elementos nuevos
print(my_other_set)

# print(my_other_set[0])

'''
Fijate que este MoureDev no se inserta
eso es debido a que los set no admiten
valores repetidos, tendria que haber dos
MoureDev, pero solo hay uno
'''
my_other_set.add("MoureDev")
print(my_other_set)

'''
El operador in permite comprobar si un elemento existe en una
estructura
'''
print("Moure" in my_other_set)
print("Mouri" in my_other_set)

my_other_set.remove("Moure") # Permite remover un elemento
print(my_other_set)

my_other_set.clear() # Elimina los datos de la lista
print(my_other_set)
print(len(my_other_set))

del my_other_set # del permite eliminar variables, objetos
# print(my_other_set) # Da error, puesto que eliminamos la variable de my_other_set - NameError: name 'my_other_set' is not defined

'''
Convertir un set en una lista es muy arriesgado
dado que durante la conversion los datos pueden
colocarse de forma aleatoria, van a desordenarse
otra vez
'''
my_set = {"Brais", "Moure", 35}
my_list = list(my_set) # Convertir set en un list
print(my_list)
print(my_list[0])

'''
union() permite unir dos sets sin que haya redundancias

En el concepto de los diagramas de venn en la teoria de
conjuntos la union es un tipo de operacion matematica
que une un conjunto de datos eliminando los datos
redundantes

La union te permite crear un set nuevo con todos los datos
de los dos sets, pero sin redundancias
'''
my_other_set = {"Kotlin", "Swift", "Python"}
my_new_set = my_set.union(my_other_set)
print(my_new_set)
'''
los sets no permiten la generacion de datos
redundantes, por eso es que cuando utilizamos
union() para unir dos sets que tienen datos
identicos, los datos que se repiten los borrara
el operador union()
'''
print(my_new_set.union(my_new_set))
print(my_new_set.union(my_new_set).union(my_set))

'''
Aqui funciona porque ya estamos agregando datos
nuevos que no estaban anteriormente

Tambien cabe recalcar que puede utilizar union para
introducir un set directamente sin necesidad de variable

    .union({"JavaScript", "C#"})
    
'''
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))

'''
difference() nos permite generar un nuevo set mediante
dos sets, de estos dos sets solo se extraeran los datos
del set a (al que le aplicas la funcion) que no tenga
el set b (al que le pasas por parametro al difference())

En la teoria de conjuntos en una diferencia un conjunto a
y b, generaran un nuevo conjunto pero con los datos para
el conjunto a que no tenga el conjunto b

La diferencia te permite crear un nuevo set pero con los datos
que no se repiten en ambos sets
'''
print(my_new_set.difference(my_set))

'''
intersection() nos permite generar un nuevo set mediante
dos sets, de estos dos sets solo se extraeran los datos
del set a (al que le aplicas la funcion) que tenga en común
para con el set b (al que le pasas por parametro al intersection())

En la teoria de conjuntos en una interseccion un conjunto a
y b, generaran un nuevo conjunto pero con los datos para
el conjunto a que tenga en común con el conjunto b

La interseccion te permite crear un nuevo set pero con los datos
que se repiten en ambos sets
'''
print(my_new_set.intersection(my_set))
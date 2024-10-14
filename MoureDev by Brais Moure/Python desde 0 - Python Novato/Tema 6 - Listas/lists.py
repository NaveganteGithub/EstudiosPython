# Listas

'''
Las listas son un tipo de dato de python que se
llama Estructura no son dato primitivo.

Las Estructuras de Python, son un tipo de dato
que nos permite agrugar varios tipos de datos,
como primitivos, tuplas, sets y más

También las Estructuras como tal pertenecen al
paradigma de la programación POO (Programacion
Orientada a Objetos), por eso es que se dice
que Python todo es un objeto (Si has aprendido
Java antes te sonara todo esto), pues no solo
es programacion funcional sino tambien Programacion
Orientada a Objetos, las listas forman parte
de la programacion orientada a objetos, en la
parte de Estructuras, todo lo que hemos visto
anteriormente es programación funcional

Ademas de que las listas nos serviran para crear
colas o pilas

Las listas son el equivalente a las matrices
o Arrays o Arreglos de Java en Python, son
estructuras que nos permiten, pero no son lo
mismo, son similares, pero no lo mismo, ya que
literalmente en una lista de Python tienes mas
funciones para operaciones con listas, que en
una Matriz de Java que tienes muy pocas opciones
y operaciones para el manejo de Arrays

Para denotar la diferencia entre un Array y una lista
    
    El Array va a tener una lista por debajo como
    estructura base, además al contrario que una
    lista un Array es inamobible por la parte de
    los datos, es Array no tiene funciones propias,
    tenemos metodos de ordenacion, pero los metodos
    de ordenacion para Arrays como el metodo
    burbuja no es propio de los Arrays, tienes
    que programarlo, no te lo da hecho
    
    Una lista no tiene nada por debajo, ademas una
    lista, al contrario que un Array, tiene operaciones
    y funciones propias, como insertado, ordenado

Para crear una lista se tiene que emplear la
funcion list() o []
'''
my_list = list()
my_other_list = []
my_list : list = list()
my_other_list : list = []

# Acceso a los elementos
print(len(my_list)) # Imprimir la longitud de la lista

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list) # Imprimir una lista
print(len(my_list))

'''
En las listas no tenemos limitacion con
respecto a los tipos de datos para
introduccir, lo que nos deja poner el
tipo de dato que queramos poner, e incluso
varios datos de diferentes tipos
'''
my_other_list = [35, 1.77, 'Brais', 'Moure']

print(type(my_other_list)) # Tipo list
print(type(my_list))
print()


# Acceder al primer elemento desde el inicio de la lista
print(my_other_list[0])

# Acceder a un elemento desde el inicio de la lista
print(my_other_list[1])
print(my_other_list[2])
# print(my_other_list[4]) # Fuera de rango


# Acceder al ultimo elemento desde el inicio de la lista
print(my_other_list[-1])

# Acceder a un elemento desde el final de la lista
print(my_other_list[-3])
print(my_other_list[-4])
# print(my_other_list[-5]) # Fuera de rango
print()

'''
Podemos utilizar el desempaquetado para
dividir los valores de la lista, para
luego guardarlos en varias variables

Para referencias mirate el tema de
desempaquetamiento de caracteres en
los strings

Recuera que si quieres utilizar el
desempaquetamiento, el numero de
valores y el numero de variables
declaradas, deben ser iguales
'''
age, height, name, surname = my_other_list
print(name)

'''
No te compliques tanto, pues la soluciones simples pueden
ahorrarte muchos problemas de logica a la hora de programar
ademas de hacer una sintaxis limpia, esto es un foco de errores
en el sentido de que te puedes equivocar a la hora de programarlo
funciona, pero no es recomendable
'''
name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)
print(name)

# Recuerda que a tu variable le puedes poner el nombre que tu quieras

print()

print(my_list + my_other_list) # Para concatenar listas
print(my_other_list + my_list)

print([1, 2, 3, 4])

# print(my_list - my_other_list) # Esto esta mal

# Funciones

'''
count() sirve para contar el numero de ocurrencias
de un valor, es decir, sirve para contar cuantas
veces se repite el elemento en la lista
'''
# print(my_other_list.count()) # Le falta algo
print(my_other_list.count("Brais"))
print(my_list.count(30))
print(my_other_list.count(30))
print()

'''
len() sirve para contar cuantos
elementos tiene una lista, como
hemos dicho anteriormente
'''
print(len(my_other_list))
print()

my_other_list.append("MoureDev") # Agrega un nuevo elemento al final de una lista 
print(my_other_list)

my_list.append(my_other_list) # Incluye un lista dentro de otra lista
print(my_list)

my_other_list.insert(1, "Rojo") # Agrega un nuevo elemento en la posicion que queramos
print(my_other_list)

my_other_list[1] = "Azul" # Modificar el elemento
print(my_other_list)

my_other_list.remove("Azul") # Eliminar el elemento que indiquemos
print(my_other_list)
'''
Dato : solo eliminara el primer elemento repetido de la lista,
si hay otro elemento que sea igual a indicado este no se borrara,
y el resto de elementos repetido tampoco
'''
print(my_list)
my_list.remove(30)
print(my_list)

my_list.pop() # Elimina el ultimo elemento de la lista, y lo devuelve como resultado
print(my_list)

my_list.pop(2) # Eliminar el elemento indicando su indice, y lo devuelve como resultado
print(my_list)

# Imprimir el elemento que se va a eliminar para posteriormente eliminarlo
print(my_list.pop(2))

'''
Guardar el elemento que se va a eliminar
en la variable para posteriormente
eliminarlo por el index
'''
my_pop_element = my_list.pop(1)
print(my_pop_element)
print(my_list)

my_list = [35, 24, 62, 52, 30, 30, 17]

del my_list[2] # Eliminar un elemento sin devolver nada, por el indice
print(my_list)

del my_list[4]
print(my_list)

my_list_2 = [35, 24, 62, 52, 30, 30, 17]

del my_list_2 # Elimina el objeto por completo (para este caso la lista), y no solo los datos
# print(my_list_2) # Da error, pues la lista ya no existe

'''
Permite encontrar la posicion del
elemento por su indice, en caso de
que elemento tuviera muchas repeticiones
nos daria la posicion del primer elemento
'''
print(my_other_list.index("Brais"))


my_new_list = my_list.copy() # Nos permite hacer una copia de la lista

my_list.clear() # Eliminar el contenido de la lista
print(my_list)
print(my_new_list)

# Voltea el contenido de la lista, es decir, invierte los valores
my_new_list.reverse()
print(my_new_list)

# Ordenar el contenido de la lista, es decir, ordena los valores
my_new_list.sort()
print(my_new_list)

# Extraer sublistas, de una lista
print(my_new_list[1:3])

'''
Ten cuidado con los lenguajes de tipado debil o dinamico puesto
que su, puesto que puede ser una gran fuente de errores de
programacion de logico, sobretodo para proyectos en el que
participan varias personas, dado que un programador puede
cambiar el tipado de una variable sumamente crucial
'''
my_list = "Hola Python";
print(my_list)
print(type(my_list))
print()
my_list = list("Hola Python");
print(my_list)
print(type(my_list))
print()
my_list = ["Hola Python"];
print(my_list)
print(type(my_list))
print()

'''
No se puede crear constantes en Python, pero si quieres crear
una variable que no quieres que te modifiquen escribela en
mayusculas, pero te la pueden modificar la mayusculas solo
sirve para decir que no quieres que modifiquen la variable
'''
MY_LIST = list()
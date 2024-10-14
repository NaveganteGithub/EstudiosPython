# Diccionarios

'''
Los diccionarios son estructuras que almacenan los datos a modo
de clave:valor, es decir no estan indexadas, sino que para cada
valor tiene una clave, y por medio de esa clave podemos acceder
al valor que queremos usar. Esta estructura nos sirve para
relacionar datos.

Funciona parecido a los hashmap

Para crear un set se tiene que emplear la
funcion dict() o {}
'''
my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

# Diferencias
# my_other_dict = {"Brais", "Moure", 35} # Esto es un set
my_other_dict = {"Nombre":"Brais", "Apellido":"Moure", "Edad":35} # Esto es un diccionario
# La clave en un diccionario no tiene porque ser un texto
my_other_dict = {"Nombre":"Brais", "Apellido":"Moure", "Edad":35, 1:"Python"}

# En cualquier estructura puedes ponerla de forma vertical
my_dict = {
            "Nombre":"Brais",
            "Apellido":"Moure",
            "Edad":35,
            "Lenguajes":"Python"
            }

'''
En los diccionarios puedes poner en la parte
del valor sub-diccionarios, o sets, o tuplas,
o listas, o numeros, o strings, etc ...
'''
my_dict = {
            "Nombre": "Brais",
            "Apellido": "Moure",
            "Edad": 35,
            "Lenguajes": {"Python", "Swift", "Kotlin"}
            }

print(my_other_dict)
print(my_dict)


my_dict = {
            "Nombre": "Brais",
            "Apellido": "Moure",
            "Edad": 35,
            "Lenguajes": {"Python", "Swift", "Kotlin"},
            1:1.77
            }
print(my_dict)

'''
len() en los diccionarios cuenta
cuantas claves tiene el diccionario
'''
print(len(my_other_dict))
print(len(my_dict))

# Funciones
print(my_dict["Nombre"]) # Sirve para acceder a un valor del diccionario mediante su clave

my_dict["Nombre"] = "Pedro" # Sirve para modificar el valor de la clave que se indique

print(my_dict["Nombre"])

'''
Da error, porque el tipo de dato
de la clave en el acceso al dato
es diferente al tipo de dato de
la clave declarada en el diccionario
para darle solucion tienes que poner
la clave del accceso con el mismo
tipo de dato con la que has declarado
en la clave de tu diccionario, es
decir, si el tipo de dato aqui

    my_dict = {
            "Nombre": "Brais",
            "Apellido": "Moure",
            "Edad": 35,
            "Lenguajes": {"Python", "Swift", "Kotlin"},
            1:1.77
            }

es numerico

    my_dict = {
            "Nombre": "Brais",
            "Apellido": "Moure",
            "Edad": 35,
            "Lenguajes": {"Python", "Swift", "Kotlin"},
       -->  1:1.77
            }

pues el acceso al dato tienes que declararlo
tambien con el tipo numerico

    print(my_dict[1])
    
y no de tipo string

    print(my_dict["1"])

'''
# print(my_dict["1"]) # Da error
print(my_dict[1]) # Sirve para acceder a un valor del diccionario mediante su clave

'''
Si intentas modificar el valor de una clave que no existe
se te creara la clave con el valor que tu hayas declarado
'''
my_dict["Calle"] = "Calle MoureDev"
print(my_dict["Calle"])
print(my_dict)

del my_dict["Calle"]
print(my_dict)

'''
El operador in buscara si hay alguna clave que coincida
con el valor pasado para la busqueda, recuerda que in
buscara en el diccionario si existe la clave que estas
declarando
'''
print("Moure" in my_dict)
print("Mouri" in my_dict)
print("Apellido" in my_dict)
'''
Recuerda que el termino de la busqueda y la clave a buscar
tiene que tener el mismo tipo de dato, ademas del mismo
nombre
'''
print("1" in my_dict) 
print(1 in my_dict)

# Te mostrara una referencia la memoria de la funcion correspondiente
print(my_dict.items)
print(my_dict.keys)
print(my_dict.values)
print(my_dict.fromkeys)

print(my_dict.items()) # Nos retorna en formato lista, las claves y los valores del diccionario agrupados
print(my_dict.keys()) # Nos retorna en formato lista, las claves del diccionario
print(my_dict.values()) # Nos retorna en formato lista, las valores del diccionario

'''
fromkeys crea un diccionario nuevo sin valores

    el primer parametro crea la claves
    el segundo parametro introduccira un valor en todas la claves (opcional)

https://www.w3schools.com/python/ref_dictionary_fromkeys.asp

En caso de que el primer valor solo pongas un texto
lo que hara from keys es desempaquetar el texto
para que cada caracter se utilizado para nombrar cada
clave del diccionario
'''
print(my_dict.fromkeys("Nombre", 1))
print(my_dict.fromkeys(("Nombre", 1)))
print(my_other_dict.fromkeys(("Nombre", 1)))
# print(my_dict.fromkeys()) # Da error

# Crea una lista vacia, con la claves que le pasamos por parametro
my_new_dict = my_other_dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)

'''
Crea una lista con la claves pasadas
por el primer parametro para despues
introduccion el valor moure a todas
la claves del diccionario
'''
my_new_dict = my_other_dict.fromkeys(("Nombre", 1, "Piso"), ("Moure"))
print(my_new_dict)

'''
Con la palabra reservada dict podemos crear
un diccionario directamente pero sin la
necesidad de utilizar otro diccionario ya
existente
'''
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)

'''
Crear un diccionario vacio el nombre de las claves
seran los nombres de la lista
'''
my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)

my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)

'''
Crear un diccionario vacio, a partir de
un diccionario existe, dejando las clave
pero eliminando los valores
'''
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

'''
Creara un nuevo diccionario con la estructura repetida
para cada valor
'''
my_new_dict = dict.fromkeys(my_dict, ("Brais", "Moure"))
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict, ["Brais", "Moure"])
print(my_new_dict)

'''
Se puede transformar de diccionario a otra estructura diferente
pero se pierden los valores solo se queda con los nombre de las
claves
'''
print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))

my_values = my_new_dict.values()
print(type(my_values)) # Imprime el tipo de objeto que me devuelve values()

print(my_new_dict.values()) # Imprime los valores del diccionario
print(list(my_new_dict.values())) # Convierte el diccionario a una lista para despues imprimirla

'''
Creara un diccionario vacio de una lista de cual es
creada a partir de los valores de un diccionario
'''
my_new_dict = dict.fromkeys(my_dict, "MoureDev")
print(dict.fromkeys(list(my_new_dict.values()))) # Para realizar esta instruccion necesitas un fromkeys como el anterior

'''
Podemos dar las vueltas a nuestro codigo,
siempre y cuando tenga algun sentido
'''

print(dict.fromkeys(list(my_new_dict.values())).keys())
# listas: colecciones ordenadas de elementos (tienen indice)
# en todas las colecciones podemos tener datos de distinto tipo
# permite tener elementos duplicados
# se crean con []

list1 = ["Maria", "Perez", 20, "soltera", "sin hijos"]
list2 = ["estudiante", "medicina", 28010]

# mostrar las listas por consola
print(list1)
print(list2)

# crear una lista vacia
lista_vacia = []
lista = list()

# unir listas
lista = list1 + list2  # el orden es importante
print(lista)
lista = list2 + list1
print(lista)

# longitud de la lista
print("Longitud de la lista:", len(lista))

# Acceso a los elementos de la lista
# indice positivo comienza por el primero, por la izquierda
print(lista[2])
# indice negativo comienza por el ultimo, por la derecha
print(lista[-2])
print(lista[len(lista) -2])

# Agregar elementos al final -> append
lista.append("morena")
print(lista)

# Agregar elementos en una determinada posicion -> insert
lista.insert(0, 1.70)
print(lista)

# Agregar varios elementos a la vez -> extend
lista.extend([1,2,3]) # los elementos tienen que ir en una coleccion
print(lista)

# Eliminar un elemento de la lista
del lista[0]
print(lista)

# Modificar un elemento
lista[-5] = "1 hijo"
print(lista)

''' slices  [begin:stop:step] '''
# mostrar todos los elementos de la lista
print("Todos:",lista[:])

# mostrar los ultimos 4 elementos de la lista
print("Ultimos 4:", lista[-4:])

# mostrar desde el tercero al sexto
print("Tercero al sexto:", lista[3:7])  # el ultimo no esta incluido

# mostrar desde el sexto al tercero
print("Sexto al tercero:", lista[7:3])   # sale vacio
print("Sexto al tercero:", lista[7:3:-1]) # asi si que funciona

# siempre se recorre de izquierda a derecha
# mostrar desde el sexto al tercero
print("Sexto al tercero:", lista[-6:2:-1])   
print("penultimo al quinto por dcha:", lista[-2:-6:-1]) 

# mostrar todos los elementos de la lista en orden inverso
print("Todos orden inverso:",lista[::-1])

# mostrar todos los elementos de la lista en orden inverso de 2 en 2
print("Todos orden inverso:",lista[::-2])

# mostrar todos los elementos de la lista  de 2 en 2
print("Todos orden:",lista[::2])

''' Operadores de pertenencia: in y not in '''
# in -> comprobar si un elemento esta en la lista
# not in -> comprueba si un elemento no existe en la lista
print("hola" in lista)
print("hola" not in lista)


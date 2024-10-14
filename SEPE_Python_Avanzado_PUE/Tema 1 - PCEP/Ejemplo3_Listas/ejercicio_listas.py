# crear una lista llamada colores con los valores rojo, verde y azul
colores = ["rojo", 'verde', 'azul']

# mostrar el tipo de la variable colores
print(type(colores))

# mostrar el contenido de la lista
print(colores)

# recorrer la lista con for in
for color in colores :
    print(color, end=" ")
print("")

# recorrer la lista con for in a traves de indice
for idx in range(len(colores)) :
    print(colores[idx], end=" ")
print("")

# mostrar en la consola el color verde (posicion) 
print(colores[1])

# Borrar el color azul por posicion
#del colores[2]
#print(colores)

# Borrar el color azul, buscar el primero y borrarlo
colores.remove("azul")  # solo borra el primero que encuentra
print("Azul eliminado:",colores)

# crear nueva lista mas_colores 
#mas_colores = list()
mas_colores = []

# en la nueva lista concatenar colores y otra lista con estos: blanco, negro, rosa, azul
mas_colores = colores + ["blanco", "negro", "rosa", "azul"]

'''  slices  '''
# mostrar los 2 ultimos elementos
print("2 ultimos elementos",mas_colores[-2:] )

# mostrar desde el ultimo al antepenultimo
print("ultimo al antepenultimo",mas_colores[-1:-4:-1] )

# mostrar hasta los 5 primeros elementos
print("5 primeros elementos",mas_colores[:5] )

# mostrar desde el segundo al cuarto
print("segundo al cuarto",mas_colores[1:4] )

# mostrar desde el primero al penultimo de 2 en 2
print("primero al penultimo, salto 2",mas_colores[:-1:2] )

# mostrar desde el penultimo al primero de 2 en 2
print("penultimo al primero, salto 2",mas_colores[-2::-2] )

# añadir el color naranja al final
mas_colores.append("naranja")

# añadir el color marron al principio
mas_colores.insert(0, "marron")
print(mas_colores)

# mostrar la longitud de la lista mas_colores
print(len(mas_colores))

# mostrar el antepenultimo elemento
print(mas_colores[-3])

# Mostrar el indice donde se encuentra el color azul
print(mas_colores.index("azul"))
#print(mas_colores.index("amarillo")) # ValueError: 'amarillo' is not in list
mas_colores.extend(['azul'])
print(mas_colores.index("azul", 7))

# Mostrar cuantos elementos azul tenemos
print("Cuantos azules?", mas_colores.count('azul'))

# Mostrar la lista invertido
print("Lista original",mas_colores)
mas_colores.reverse()
print("Lista invertida", mas_colores)

# Ordenar la lista por el metodo sort
#mas_colores.sort()   # orden ascendente
#print("Sort:", mas_colores )
print(sorted(mas_colores))

#mas_colores.sort(reverse=True)   # orden descendente
#print("Sort descendente:", mas_colores )
print(sorted(mas_colores, reverse=True))

# principio de inmutabilidad con sorted, me muestra la lista original, intacta
print("Inmutabilidad:", mas_colores)

# Eliminar todos los elementos de la lista
# mas_colores = []   crear una lista vacia y cambiar la direccion de memoria de la variable mas_colores
mas_colores.clear()
print(mas_colores)
students = []
'''
split lo que hace es separar cada linea en una lista y el texto de cada linea
separado por un delimitador sera guardado en una posicion de cada lista
'''
with open("names.csv", "r") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")


'''
with open("names.txt", "r") as file:
    for name in sorted(file, reverse=True):
        print("hello,", name.rstrip()) # rstrip quita los espacios en blanco de la derecha
'''

'''
with open("names.txt", "r") as file:
    for name in sorted(file):
        print("hello,", name.rstrip())
'''

'''
names = []

with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")
'''

'''
with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())
'''

'''
with es una funcion para ejecutar algo con un recurso,
el "as" solo es necesario cuando quieres crear una variable
para almacenar, esto es mejor que file.close() porque asi
se evita la corrupcion de archivos

with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())
'''

'''
name = input("What´s your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")
'''
'''
name = input("What´s your name? ")

# file = open("names.txt", "w") # open es una funcion para abrir archivos en este caso en modo escritura, devolvera la direccion del fichero
file = open("names.txt", "a") # en este caso estamos leyendo, escribiendo y ejecutando el archivo
# file.write(name) # escribe en el fichero abrierto
file.write(f"{name}\n")
# file.close # cerrara el fichero
'''


'''
names = []

for _ in range(3):
    names.append(input("What´s your name? "))

for name in sorted(names): # sorted es una funcion que devuelve la lista ordenada
    print(f"hello, {name}")
'''
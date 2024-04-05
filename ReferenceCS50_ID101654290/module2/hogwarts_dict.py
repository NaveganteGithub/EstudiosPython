"""
students = ["Hermione", "Harry", "Ron"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]
"""
"""
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])


for student in students:
    print(student, students[student], sep=", ")

"""

"""
Normalmente se van a trabajar con tablas SQL por lo que hace
imprescindible realizar una estrutura que soporte dichas tablas
para ello se utilizara una combinacion de diccionarios y filas

Cada palabra clave de cada diccionario es el nombre de una columna
todos los diccionarios deben tener el mismo numero de claves y valores
ademas de tener los mismos para sus claves, la lista hara como de
soporte para poder guardar todas y cada una de las filas de la tabla
guardando los diccionarios

Clave = Columna
Valor = Fila
"""

students = [
    {"name":"Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name":"Harry", "house":"Gryffindor", "patronus":"Stag"},
    {"name":"Ron", "house":"Gryffindor", "patronus":"Jack Russell terrier"},
    {"name":"Draco", "house":"Slytherin", "patronus": None} # None representa un valor vacio o que no hay nada
]

# Este for permite extraer del diccionario los valores de las columnas name y house
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
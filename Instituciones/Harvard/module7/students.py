import csv

students = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row) # Incrustara todo el diccionario

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")

'''name = input("What´s your name? ")
home = input("Where´s your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"home": home, "name": name})'''


'''name = input("What´s your name? ")
home = input("Where´s your home? ")

with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])'''


'''students = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

# key=lambda student: student["name"] equivale a la funcion get_house anterior que servira para ordenar el diccionario

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")'''

'''students = []

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})

# key=lambda student: student["name"] equivale a la funcion get_house anterior que servira para ordenar el diccionario

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")'''

'''students = []

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name": row[0], "home": row[1]})

# key=lambda student: student["name"] equivale a la funcion get_house anterior que servira para ordenar el diccionario

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")'''

'''
students = []

with open("students.csv", "r") as file:
    for line in file:
        name, home = line.rstrip().split(",")
        student = {"name": name, "home": home}
        students.append(student)

# key=lambda student: student["name"] equivale a la funcion get_house anterior que servira para ordenar el diccionario

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
'''

'''

students = []

with open("names.csv", "r") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

# key=lambda student: student["name"] equivale a la funcion get_house anterior que servira para ordenar el diccionario

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
'''

'''
students = []

with open("names.csv", "r") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)


Si creas una funcion que devuelva un texto sorted
puede utilizarlo para ordenar diccionarios


def get_house(student):
    return student["house"]

for student in sorted(students, key=get_house, reverse=True):
    print(f"{student['name']} is in {student['house']}")
'''

'''
students = []

with open("names.csv", "r") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in sorted(students):
    print(f"{student['name']} is in {student['house']}")
'''
import csv

# Leer archivos csv como lista
with open("empleado.csv", newline="") as empleado_csv:
    datos = csv.reader(empleado_csv, delimiter=",")  # Devuelve un Objeto con listas

    for item in datos:
        print(item)  # Lista

    print("---------------------------")

with open("empleado.csv", newline="") as empleado_csv:
    datos = csv.reader(empleado_csv, delimiter=",")

    for item in datos:
        print("_".join(item))

    print("---------------------------")

# Leer archivos csv como diccionario
with open("empleado.csv", newline="") as empleado_csv:
    datos = csv.DictReader(empleado_csv, delimiter=",")  # Instanciamos una clase que contiene diccionarios

    for item in datos:
        print(item)  # Diccionarios
        print("ID:", item['Id'])
        print("Nombre:", item['Nombre'])
        print("Apellido:", item['Apellido'])
        print("Email:", item['Email'])
        print("Sueldo:", item['Sueldo'])

    print("---------------------------")


# Crear diccionarios con cabeceras personalizadas
with open("empleado.csv", newline="") as empleado_csv:
    cabeceras = ['Id', 'Nombre', 'Apellido', 'Correo', 'Salario']
    datos = csv.DictReader(empleado_csv, delimiter=",", fieldnames=cabeceras)

    for item in datos:
        print(item['Nombre'], item['Salario'], item['Correo'])

    print("---------------------------")


import csv

with open('empleados.csv',newline='') as empleadoscsv:
    datos = csv.reader(empleadoscsv, delimiter=",")
    for item in datos:
        print(item) # como lista ['Id', 'Nombre', 'Apellido', 'Email', 'Sueldo']
    print("------------------------")

with open('empleados.csv',newline='') as empleadoscsv:
    datos = csv.reader(empleadoscsv, delimiter=",")
    for item in datos:
        print("-".join(item)) # como texto Id-Nombre-Apellido-Email-Sueldo
    print("------------------------")

with open('empleados.csv',newline='') as empleadoscsv:
    datos = csv.DictReader(empleadoscsv, delimiter=",")
    for item in datos:
        print(item) # como diccionario {'Id': '1', 'Nombre': 'Juan', 'Apellido': 'Lopez', 'Email': 'juan@gmail.com', 'Sueldo': '47000'}
        print("ID:", item['Id'])
        print("Nombre:", item['Nombre'])
        print("Apellido:", item['Apellido'])
        print("Email:", item['Email'])
        print("Sueldo:", item['Sueldo'])
    print("------------------------")

with open('empleados.csv',newline='') as empleadoscsv:
    cabeceras = ['Id','Nombre','Apellido','Email','Sueldo']
    datos = csv.DictReader(empleadoscsv, delimiter=",", fieldnames=cabeceras)
    for item in datos:
        print(item['Nombre'], item['Sueldo']) 
    print("------------------------")
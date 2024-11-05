import csv

with open("archivo.csv", "wt", encoding="utf-8") as archivo:
    fichero_csv = csv.writer(archivo, delimiter=":", lineterminator="\n")
    fichero_csv.writerow(["ID", "Nombre", "Sueldo"])
    fichero_csv.writerows([[1, "Daniel", 1200.25],
                           [2, "Sara", 4150.56],
                           [3, "Samuel", 45460],
                           [4, "Alber", 1542.30]])

with open("archivo.csv", "rt", encoding="utf-8") as archivo:
    fichero_csv = csv.reader(archivo, delimiter=":", lineterminator="\n")

    # Opcion 1
    lista = list(fichero_csv)
    print(lista)

    archivo.seek(0)
    fichero_csv = csv.reader(archivo, delimiter=":", lineterminator="\n")

    # Opcion 2
    lista = [i for i in fichero_csv]
    print(lista)

    archivo.seek(0)
    fichero_csv = csv.reader(archivo, delimiter=":", lineterminator="\n")

    # Opcion 3
    for i in fichero_csv:
        print(i)


    print(fichero_csv.line_num)

with open("archivo2.csv", "wt", encoding="utf-8") as archivo:
    fichero_csv = csv.DictWriter(f=archivo, fieldnames=["Id", "Nombre", "Sueldo"], delimiter=";", lineterminator="\n")
    fichero_csv.writeheader()
    fichero_csv.writerow({"Id": 1, "Nombre": "Daniel", "Sueldo": 1200.25})
    fichero_csv.writerows([{"Id": 2, "Nombre": "Sara", "Sueldo": 4150.56},
                            {"Id": 3, "Nombre": "Samuel", "Sueldo": 45460},
                            {"Id": 4, "Nombre": "Alber", "Sueldo": 1542.30}])


with open("archivo2.csv", "rt", encoding="utf-8") as archivo:
    fichero_csv = csv.DictReader(f=archivo, fieldnames=["Id", "Nombre", "Sueldo"], delimiter=";", lineterminator="\n")

    for i in fichero_csv:
        print(i)
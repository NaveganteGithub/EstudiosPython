import csv

with open("datos.csv", "w", encoding="utf-8") as datos:
    fichero = csv.writer(datos, delimiter=";")

    fichero.writerows(iter([
        ["Nombre", "Precio", "Genero"],
        ["Daniel", 2600, "H"],
        ["Andrea", 2000, "M"],
        ["Pedro", 2100, "H"],
        ["Sara", 3000, "M"]
    ])
    )

    fichero.writerow(["Alejandro", 2900, "H"])


with open("datos2.csv", "w", encoding="utf-8") as datos:
    cabecera = ["Nombre", "Precio", "Genero"]
    fichero = csv.DictWriter(datos, delimiter=";", fieldnames=cabecera)

    fichero.writeheader()
    fichero.writerow({"Nombre": "Daniel", "Precio": 2600, "Genero": "H"})
    fichero.writerow({"Nombre": "Andrea", "Precio": 2000, "Genero": "M"})
    fichero.writerow({"Nombre": "Pedro", "Precio": 2100, "Genero": "H"})


with open("datos.csv", "r", encoding="utf-8") as datos:
    lectura = csv.reader(datos, delimiter=";")
    print([l for l in lectura])

with open("datos2.csv", "r", encoding="utf-8") as datos:
    lectura = csv.DictReader(datos, delimiter=";")
    print([l for l in lectura])
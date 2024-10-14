import csv

with open("productos.csv", 'w', encoding="utf-8", newline="") as productos_csv:
    puntero = csv.writer(productos_csv, delimiter=",")

    puntero.writerow(['ID', "Descripcion", 'Precio'])

    puntero.writerow([1, "Teclado", 129.50])
    puntero.writerow([2, "Raton", 9.50])
    puntero.writerow([3, "Impresora", 50.10])
    puntero.writerow([4, "Portatil", 1029.90])
    puntero.writerow([4, "Ofuscador", 1029.90])

with open("productos_2.csv", "w", encoding="utf-8", newline="") as productos_csv:
    cabeceras = ['ID', 'Descripcion', 'Precio']

    puntero = csv.DictWriter(productos_csv, fieldnames=cabeceras)

    puntero.writeheader()
    puntero.writerow({'ID': 1, 'Descripcion': 'Pantalla', 'Precio': 129.20})
    puntero.writerow({'ID': 2, 'Descripcion': 'Teclado', 'Precio': 23.20})
    puntero.writerow({'ID': 3, 'Descripcion': 'Scanner', 'Precio': 29.17})
    puntero.writerow({'ID': 4, 'Descripcion': 'Impresora', 'Precio': 78.10})
    puntero.writerow({'ID': 5, 'Descripcion': 'Raton', 'Precio': 9.20})


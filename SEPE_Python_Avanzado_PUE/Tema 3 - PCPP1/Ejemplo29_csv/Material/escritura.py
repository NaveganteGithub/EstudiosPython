import csv

with open('productos.csv', 'w', newline='') as csvproductos:
    writer = csv.writer(csvproductos, delimiter=",")
    writer.writerow(['ID','Descripcion','Precio'])
    writer.writerow([1, 'Pantalla', 129.50])
    writer.writerow([2, 'Teclado', 49.95])
    writer.writerow([3, 'Raton', 18])
    writer.writerow([4, 'Scanner', 450])
    writer.writerow([5, 'Impresora', 89.90])

with open('productos2.csv', 'w', newline='') as csvproductos:
    cabeceras = ['ID','Descripcion','Precio']
    writer = csv.DictWriter(csvproductos, fieldnames=cabeceras)

    writer.writeheader()
    writer.writerow({'ID':1, 'Descripcion':'Pantalla', 'Precio':129.5})
    writer.writerow({'ID': 2, 'Descripcion': 'Teclado', 'Precio': 49.95})
    writer.writerow({'ID': 3, 'Descripcion': 'Raton', 'Precio': 18})
    writer.writerow({'ID': 4, 'Descripcion': 'Scanner', 'Precio': 450})
    writer.writerow({'ID': 5, 'Descripcion': 'Impresora', 'Precio': 89.90})


# pip install numpy
import numpy as np
lista = [[1,2,3,4],[5,6,7,8]]
datos = np.asarray(lista)
np.savetxt("output.csv", # Archivo de salida
datos.T, # Trasponemos los datos
delimiter=",") # Para que sea un CSV de verdad
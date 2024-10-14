import numpy as np

lista = [[1, 2, 3, 4], [5, 6, 7, 8]]
datos = np.asarray(lista)
np.savetxt("output.csv",          # Archivo de salida
           datos.T,                     # Trasponemos los datos
           delimiter=",")               # Para que sea un CSV de verdad

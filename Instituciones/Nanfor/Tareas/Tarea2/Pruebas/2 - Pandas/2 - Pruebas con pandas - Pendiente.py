import numpy as np
import pandas as pd

# --------------------------------------------- SERIES --------------------------------------------- #
"""
Series crea un array de una dimension, y cuando se imprima la lista
se imprimira sus valores con su index y al final los tipos de datos 
que contiene
"""
serie_1 = pd.Series([1213, 5465])
print("La serie serie_1 es la siguiente", serie_1, sep='\n')

serie_2 = pd.Series({'DAM':7.5, 'DAW':4.5, 'ASIR':6.5})
print("La serie serie_2 es la siguiente", serie_2, sep='\n')

# Size devuelve el numero de posiciones que tiene la Serie
print("La serie serie_1 tiene", serie_1.size, "posiciones.")
print("La serie serie_2 tiene", serie_2.size, "posiciones.")

# index devuelve el rango que ocupa ciertos caracteres en la Serie
serie_3 = pd.Series([1213, 1213, 1213, 5465, 5465, 1561, 1561, 1561, 1561, 1561, 1561])
serie_4 = pd.Series(['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'b', 'c', 'c', 'c'])

print("La serie serie_3 tiene", serie_3.index, "posiciones.")
print("La serie serie_4 tiene", serie_4.index, "posiciones.")

# dtype devuelve el tipo de datos que tiene una Serie
print(serie_1.dtype)
print(serie_2.dtype)
print(serie_3.dtype)
print(serie_4.dtype)

# --------------------------------------------- DATAFRAMES --------------------------------------------- #

"""
DataFrame creara una tabla a partir de un diccionario, que luego 
va a ser imprimida, mostrara las claves del diccionario como el
nombre de las columnas y los valores del diccionario en una
fila cada uno

AVISO: el numero de valores tiene que tener la cantidad exacta
para forme una tabla completa, sino dara error
"""
dataframe_1 = pd.DataFrame(
            {'DAM':[7.5, 5.0, 9.1], 
            'DAW':[4.5, 7.5, None], 
            'ASIR':[6.5, 4.2, 7.7]
            }
         )

'''
dataframe_1 = pd.DataFrame(
            {'DAM':[7.5, 5.0, 9.1], 
            'DAW':[4.5, 7.5], 
            'ASIR':[6.5, 4.2, 7.7]
            }
         )
''' # Da error, porque el numero de valores no es suficiente para crear una tabla perfecta

print(dataframe_1)

"""
DataFrame creara una tabla a partir de una lista, que luego 
va a ser imprimida, mostrara las listas del parametro data
como los valores de cada fila y los valores del parametro
column como los nombres de la columna

AVISO: el numero de valores tiene que tener la cantidad exacta
para forme una tabla completa, sino dara error
"""
dataframe_2 = pd.DataFrame(
            columns=['Nombre del producto', 'Cantidad vendida', 'Cantidad en stock', 'Precio', 'Rebaja'],
            data=[
                ['Manzanas', 78, 150, 0.75, True],
                ['Platanos', 68, 220, 0.55, False]
                ]
         )

print(dataframe_2)

"""
DataFrame creara una tabla a partir de una lista cuyos valores seran aleatorios,
el primer parametro sera utilizado para declarar el nombre de las columnas, el
segundo parametro sera utilizado para declarar randn de la libreria numpy para
crear los valores aleatorios donde el primer parametro de randn sera el numero
de filas que quieras que tenga la tabla, y el segundo parametro sera el numero
de columnas que tengas especificado en el columns del DataFrame
"""
dataframe_3 = pd.DataFrame(
            columns=['a', 'b', 'c', 'd', 'e'],
            data=np.random.randn(7, 5)
         )

print(dataframe_3)

# Esta opcion es mas dinamica
nombre_columnas = ['a', 'b', 'c', 'd', 'e']
numero_columnas = len(nombre_columnas)

dataframe_4 = pd.DataFrame(
            columns=nombre_columnas,
            data=np.random.randn(7, numero_columnas)
         )

print(dataframe_4)


# read_csv leera un archivo csv con los datos que le inquemos


# read_excel leera un archivo csv con los datos que le inquemos


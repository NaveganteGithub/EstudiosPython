import pandas as pd
import matplotlib.pyplot as mp

"""
La libreria pandas tiene buena integracion con la libreria matplotlib
para usarla
   1- Se tiene que crear un diccionario con una cabecera de valores (Platos del dia)
   y con sus repectivos valores (Todos los demas valores de todas las claves del diccionario
   salvo platos del dia que esa sera la cabecera)
   2- Se tiene que usar la funcion DataFrame de pandas y guardar el resultado en una variable
   3- Se tiene que usar la funcion subplots de la libreria matplotlib
   4- Se usara la variable del Dataframe para llamar a la funcion plot y ahi se especifica
   el parametro "x" que se le pasara la cabecera del diccionario y el parametro "y" que contendra
   una clave del resto del diccionario que contenga datos
   5- Se usara show para visualizar el diccionario
"""

stock = {"Platos del dia": ['Macarrones con queso', 'Sopa de pescado', 
              'Salmon a la plancha con patatas', 'Ensalada', 
              'Filete de ternera con patatas', 'Pollo asado en su salsa', 
              'Pisto con calabacin'],
           "Avenida de Rafael Alberti": [111, 321, 520, 232, 512, 552, 222],
           "Avenida de palomeras": [343, 635, 212, 341, 251, 122, 159],
           "Avenida Buenos Aires": [123, 565, 215, 122, 320, 120, 252],
           "Avenida de la Albufera": [147, 536, 521, 200, 124, 632, 411],
           "Calle Serrano": [111, 202, 500, 302, 112, 212, 323],
           "Calle Alcala": [563, 210, 362, 332, 235, 561, 251],
           "Calle Gran Via": [123, 213, 564, 423, 561, 210, 231]
           }

diccionario_DataFrame = pd.DataFrame(stock)

ventana_creada, axes = mp.subplots()

diccionario_DataFrame.plot(x="Platos del dia", y="Avenida de Rafael Alberti", ax=axes)
diccionario_DataFrame.plot(x="Platos del dia", y="Calle Gran Via", ax=axes)

mp.show()
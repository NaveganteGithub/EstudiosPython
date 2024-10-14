import pandas as pd
import matplotlib.pyplot as mp

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

diccionario_DataFrame.plot(ax=axes)

mp.savefig('diagrama_2.png')
mp.show()
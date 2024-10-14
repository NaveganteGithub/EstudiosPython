import matplotlib.pyplot as mp

ventana_creada, axes = mp.subplots()

# Se crean los titulos para cada marcador de cada linea
platos_dia = ['Macarrones con queso', 'Sopa de pescado', 
              'Salmon a la plancha con patatas', 'Ensalada', 
              'Filete de ternera con patatas', 'Pollo asado en su salsa', 
              'Pisto con calabacin']

# Se crean los datos que se van a utilizar para cada columna
ventas = {"Avenida de Rafael Alberti": [20, 23, 23, 21, 10, 26, 30],
           "Avenida de palomeras": [45, 65, 74, 58, 23, 14, 21],
           "Avenida Buenos Aires": [88, 47, 58, 63, 75, 23, 111],
           "Avenida de la Albufera": [23, 15, 32, 56, 87, 144, 52, 12]
           }

stock = {"Avenida de Rafael Alberti": [111, 321, 520, 232, 512, 552, 222],
           "Avenida de palomeras": [343, 635, 212, 341, 251, 122, 159],
           "Avenida Buenos Aires": [123, 565, 215, 122, 320, 120, 252],
           "Avenida de la Albufera": [147, 536, 521, 200, 124, 632, 411]
           }

"""
Volviendo a la funcion plot, se pueden agregar mas parametro que 
se pueden utilizar para personalizar la grafica 
    - color sirve para determinar el color de la linea
    - marker sirve para determinar que simbolo tendra cada marcador de la linea
    - linestyle sirve para determinar el estilo que tendra la linea
"""
axes.plot(platos_dia, ventas["Avenida de Rafael Alberti"], color='tab:red', marker='.', linestyle='dashed')
axes.plot(platos_dia, stock["Avenida de Rafael Alberti"], color='tab:green', marker='^', linestyle='dotted')

axes.plot(platos_dia, ventas["Avenida de palomeras"], color='tab:blue', marker='.', linestyle='dashed')
axes.plot(platos_dia, stock["Avenida de palomeras"], color='tab:purple', marker='^', linestyle='dotted')

mp.show()
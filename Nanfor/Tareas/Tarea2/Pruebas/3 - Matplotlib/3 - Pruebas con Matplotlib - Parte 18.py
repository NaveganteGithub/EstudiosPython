import matplotlib.pyplot as mp

# Para crear una ventana con multiples diagramas, puedes especificar estos parametros filas,columnas,sharey
ventana_creada, axes = mp.subplots(2,3, sharey=True)

platos_dia = ['Macarrones con queso', 'Sopa de pescado', 
              'Salmon a la plancha con patatas', 'Ensalada', 
              'Filete de ternera con patatas', 'Pollo asado en su salsa', 
              'Pisto con calabacin']

ventas = {"Avenida de Rafael Alberti": [20, 23, 23, 21, 10, 26, 30],
           "Avenida de palomeras": [45, 65, 74, 58, 23, 14, 21],
           "Avenida Buenos Aires": [88, 47, 58, 63, 75, 23, 111],
           "Avenida de la Albufera": [23, 15, 32, 56, 87, 144, 52],
           "Calle Serrano": [20, 23, 51, 20, 35, 10, 25],
           "Calle Alcala": [32, 35, 65, 96, 21, 45, 23]
           }

stock = {"Avenida de Rafael Alberti": [111, 321, 520, 232, 512, 552, 222],
           "Avenida de palomeras": [343, 635, 212, 341, 251, 122, 159],
           "Avenida Buenos Aires": [123, 565, 215, 122, 320, 120, 252],
           "Avenida de la Albufera": [147, 536, 521, 200, 124, 632, 411],
           "Calle Serrano": [111, 202, 500, 302, 112, 212, 323],
           "Calle Alcala": [563, 210, 362, 332, 235, 561, 251]
           }

# Se puede especificar varios tipos de diagramas
axes[0, 0].bar(platos_dia, ventas["Avenida de Rafael Alberti"], color='tab:red', linestyle='dashed')
axes[0, 0].plot(platos_dia, stock["Avenida de Rafael Alberti"], color='tab:green', marker='^', linestyle='dotted')

axes[0, 1].bar(platos_dia, ventas["Avenida de palomeras"], color='tab:red', linestyle='dashed')
axes[0, 1].plot(platos_dia, stock["Avenida de palomeras"], color='tab:green', marker='^', linestyle='dotted')

axes[0, 2].bar(platos_dia, ventas["Avenida Buenos Aires"], color='tab:red', linestyle='dashed')
axes[0, 2].plot(platos_dia, stock["Avenida Buenos Aires"], color='tab:green', marker='^', linestyle='dotted')

axes[1, 0].bar(platos_dia, ventas["Avenida de la Albufera"], color='tab:red', linestyle='dashed')
axes[1, 0].plot(platos_dia, stock["Avenida de la Albufera"], color='tab:green', marker='^', linestyle='dotted')

axes[1, 1].bar(platos_dia, ventas["Calle Serrano"], color='tab:red', linestyle='dashed')
axes[1, 1].plot(platos_dia, stock["Calle Serrano"], color='tab:green', marker='^', linestyle='dotted')

axes[1, 2].bar(platos_dia, ventas["Calle Alcala"], color='tab:red', linestyle='dashed')
axes[1, 2].plot(platos_dia, stock["Calle Alcala"], color='tab:green', marker='^', linestyle='dotted')

mp.show()
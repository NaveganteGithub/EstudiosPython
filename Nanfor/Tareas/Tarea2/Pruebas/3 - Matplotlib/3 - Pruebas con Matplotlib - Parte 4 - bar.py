import matplotlib.pyplot as mp

ventana_creada, axes = mp.subplots()

""" 
Con bar crear un esquema de barras verticales, donde en este caso
        - la primera columna tendra una altura de 5
        - la segunda columna tendra una altura de 8
        - la tercera columna tendra una altura de 2
        - la cuarta columna tendra una altura de 1
"""
axes.bar([1,2,3,4], [5,8,2,1])

# Con show visualizaras la imagen 
mp.show()
import numpy as np
import matplotlib.pyplot as mp

ventana_creada, axes = mp.subplots()

""" 
Con imshow se puede crear un mapa de color
"""
axes.imshow(np.random.random((2,2)))

# Con show visualizaras la imagen 
mp.show()
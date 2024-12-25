import matplotlib.pyplot as mp

ventana_creada, axes = mp.subplots()

""" 
Con pie se puede dibujar un diagrama de sectores, donde cada 
posicion de la lista representa un sector y los valores que
ocupa cada posicion sera la cantidad de espacio que ocupe el
sector
"""
axes.pie([1,2,3,4,5,7,49])

# Con show visualizaras la imagen 
mp.show()
import matplotlib.pyplot as mp

ventana_creada, axes = mp.subplots()

""" 
Con plot permite crear un diagrama de lineas, donde en este caso 
        - el primer punto esta en las coordenadas x=1 y=5
        - el segundo punto esta en las coordenadas x=2 y=8
        - el tercero punto esta en las coordenadas x=3 y=2
        - el cuarto punto esta en las coordenadas x=4 y=1
"""
axes.plot([1,2,3,4], [5,8,2,1])

# Con show visualizaras la imagen 
mp.show()
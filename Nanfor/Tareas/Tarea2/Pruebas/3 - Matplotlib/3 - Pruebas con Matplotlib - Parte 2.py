import matplotlib.pyplot as mp

""" 
Con el modulo pyplot de la libreria matplotlib 
se pueden crear graficas

El codigo siguiente permite crear un diagrama de dispersion
o puntos, que son esos esquemas con coordenadas y puntos

Con subplots crearemos la figura que es la ventana o pagina 
o region donde se dibujara los ejes del esquema
"""
ventana_creada, axes = mp.subplots()

""" 
Con scatter se puede especificar la posicion de los puntos, donde en este caso
        - el primer punto esta en las coordenadas x=3 y=5
        - el segundo punto esta en las coordenadas x=1 y=2
        - el tercero punto esta en las coordenadas x=5 y=2
        - el cuarto punto esta en las coordenadas x=5 y=2
"""
axes.scatter(x = [3,1,5,2], y = [5,2,2,9])

# Con savefig crearas la imagen
mp.savefig("diagrama_1.png")

# Con show visualizaras la imagen 
mp.show()
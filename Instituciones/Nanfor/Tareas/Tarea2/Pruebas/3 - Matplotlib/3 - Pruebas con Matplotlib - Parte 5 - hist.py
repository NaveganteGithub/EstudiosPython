import matplotlib.pyplot as mp

ventana_creada, axes = mp.subplots()

""" 
plot y bar son muy parecidos a scatter, pero ahora se va a mirar
una funcion diferente

Con hist crear un histograma, donde el primer parametro se indica 
la lista con los valores que se repiten que frecuencia, mientras
que en bins se indica el numero de cajas o columnas que tendra
el diagrama, como hay cuatro valores que son el 1,2,3 y 4, pues
se pondra en bins 4 para indicar que queremos cuatro columnas para
cuatro valores diferentes que se repiten
"""
mp.hist([1,1,1,1,1,1,1,1,1,1,2,3,3,3,3,3,3,3,4,4,4], bins=4)

# Opcionalmente puedes utilizar xlabel y ylabel para indicar un nombre para los valores y la frecuencia

mp.xlabel('Valores')
mp.ylabel('Frecuencia')

# Con show visualizaras la imagen 
mp.show()
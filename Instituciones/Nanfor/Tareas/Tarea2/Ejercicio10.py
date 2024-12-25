import pandas as pd
import matplotlib.pyplot as mp

anual = pd.read_csv('Tarea2\\annual.csv', sep=',')

lista_anual_fuentes = list(anual.loc[:, 'Source'].drop_duplicates())

region, axes = mp.subplots()

for contenido_lista in lista_anual_fuentes:
    consulta = anual.query(('Source == \'' + contenido_lista + '\''))
    
    lista_tiempo = list(consulta.loc[:, 'Year'])
    media = list(consulta.loc[:, 'Mean'])
    
    diccionario_grafica = {
            "Años":lista_tiempo, 
            "Medias":media
            }
    
    diccionario_DataFrame = pd.DataFrame(diccionario_grafica)
    diccionario_DataFrame.plot(x="Años", y="Medias", ax=axes)

    # print(diccionario_DataFrame)

axes.legend(lista_anual_fuentes)

mp.show()
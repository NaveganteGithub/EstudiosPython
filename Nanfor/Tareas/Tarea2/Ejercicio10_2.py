import pandas as pd
import matplotlib.pyplot as mp

anual = pd.read_csv('Tarea2\\annual.csv', sep=',')
diccionario_DataFrame = pd.DataFrame(anual)

lista_fuentes = list(anual.loc[:, 'Source'].drop_duplicates())

region, axes = mp.subplots()

for fuente in lista_fuentes:
    consulta = diccionario_DataFrame.query(('Source == \'' + fuente + '\''))
    consulta.plot(x="Year", y="Mean", ax=axes)

axes.legend(lista_fuentes)
mp.show()
import pandas as pd
import matplotlib.pyplot as mp

cont = 0
lista_colores = ['orange','blue']

anual = pd.read_csv('Tarea2\\annual.csv', sep=',')
diccionario_DataFrame = pd.DataFrame(anual)

lista_fuentes = list(anual.loc[:, 'Source'].drop_duplicates())

region, axes = mp.subplots(1,2, sharey=True)
region.set_figwidth(1920)

for fuente in lista_fuentes:
    consulta = diccionario_DataFrame.query(('Source == \'' + fuente + '\''))
    year = list(consulta.loc[:, 'Year'])
    mean = list(consulta.loc[:, 'Mean'])
    axes[cont].plot(year, mean, color='tab:'+lista_colores[cont])
    axes[cont].legend([fuente], loc='upper left')
    cont += 1

mp.show()
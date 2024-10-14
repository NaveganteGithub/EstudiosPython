#!/usr/bin/env python
# coding: utf-8

# # DataFrames

# In[1]:


# importar el modulo Pandas
import pandas as pd


# In[2]:


# crear un dataframe a partir de una lista
data2 = [['Juan', 4.5], ['Pedro', 8.9],['Estefania',1.4], ['Ana',5.6],['Esteban',7.8]]
columnasNombres = ['Nombre','Nota']
filas = list(range(len(data2)))  # [0,1,2,3,4]
df = pd.DataFrame(data2, columns=columnasNombres, index=filas)
df


# In[3]:


# Obtener informacion
df.info  # atributo, sin parentesis


# In[4]:


# Mostrar la forma del dataframe (num_filas, num_columnas)
df.shape   


# In[5]:


# tamaño del dataframe (num_filas * num_columnas)
df.size


# In[6]:


# Mostrar los nombres de las columnas
df.columns


# In[7]:


# Mostrar los indices
df.index


# In[8]:


# Tipos de datos de las columnas
df.dtypes


# In[9]:


# Mostrar las primeras 3 filas
df.head(3)


# In[10]:


# Mostrar las 3 ultimas filas
df.tail(3)


# In[11]:


# crear un dataframe a partir de un diccionario
dictNombreNotas1 = { 
"Id": [1,2,3,4,5] ,
"Nombre" : ['Juan', 'Pedro','Estefania', 'Ana', 'Esteban'],
"Apellido": ['Garcia', 'Sanchez', 'Lopez', 'Garcia', 'Gonzalez' ],
"Nota": [4.5, 8.9, 1.4, 5.6, 7.8]
}
dfDesdeDict1 = pd.DataFrame(dictNombreNotas1)
dfDesdeDict1


# In[12]:


# Otra forma de crear el dataframe a partir de un diccionario
dictNombreNotas2 = [{'Id':6, 'Nombre':'Silvia', 'Apellido':'Gonzalez','Nota':5.5},
                   {'Id':7, 'Nombre':'Pedro', 'Apellido':'Perez','Nota':8.9}]
dfDesdeDict2 = pd.DataFrame(dictNombreNotas2)
dfDesdeDict2


# In[13]:


# Acceso a los datos:
# iloc[] -> acceso por posicion[fila,columna]
dfDesdeDict1.iloc[2,3]


# In[14]:


# Queremos obtener los datos desde la fila 1 a la 3
dfDesdeDict1.iloc[1:3]  # solo la fila 1 y 2 con todas las columnas
dfDesdeDict1.iloc[1:3,] # solo la fila 1 y 2 con todas las columnas
dfDesdeDict1.iloc[1:3,:]  # solo la fila 1 y 2 con todas las columnas  [rango_filas, rango_columnas]


# In[15]:


# Queremos obtener los datos desde la fila 1 con las 3 primeras columnas
dfDesdeDict1.iloc[1:3:3]


# In[16]:


# Queremos obtener los datos desde la fila 1 hasta la 3 con las 3 primeras columnas
dfDesdeDict1.iloc[1:3,:3]


# In[17]:


# Mostrar todas las filas desde 0, solo 2 primeras columnas
dfDesdeDict1.iloc[:,:2]
dfDesdeDict1.iloc[:,0:2]  # es lo mismo


# In[18]:


#También funciona para seleccionar diferentes columnas y/o filas:
dfDesdeDict1.iloc[1:4,[1,3]] #mostrar ciertas columnas: nombre y nota

dfDesdeDict1.iloc[[1,4],[1,3]] #mostrar ciertas filas y ciertas columnas


# In[19]:


# Acceso a los datos:
# loc[] -> acceso por indice[nombre_indice_fila]
dfDesdeDict1.loc[2]


# In[20]:


# Mostrar la fila 2 y fila 4
dfDesdeDict1.loc[[2,4]]


# In[21]:


# Mostrar desde el indice de la fila 2 a la fila 4
dfDesdeDict1.loc[2:4]


# In[22]:


# crear un dataframe a partir de una lista
data2 = [['Juan', 4.5], ['Pedro', 8.9],['Estefania',1.4], ['Ana',5.6],['Esteban',7.8]]
columnas = ['Nombre','Nota']
filas = [10,11,12,13,14]
df = pd.DataFrame(data2, columns=columnasNombres, index=filas)
df


# In[23]:


# iloc -> accedemos por el orden de la fila
df.iloc[1,:]  # 1 representa la segunda fila


# In[24]:


# loc -> accedemos por el nombre del indice de la fila
#df.loc[1]  # error porque el indice 1 no existe
df.loc[11]


# In[25]:


# Solo la nota de Pedro [indice,['columna']]
df.loc[11,['Nota']]


# In[26]:


# Solo la nota de Pedro y Ana [[indice, indice],['columna']]
df.loc[[11,13],['Nota']]


# In[27]:


# no puedo poner rangos
#df.loc[[11:13],['Nota']]  # error
df.loc[11:13]['Nota']  # si funciona


# In[28]:


# Solo la nota de Pedro df['columna'].loc[indice]
df['Nota'].loc[11]


# In[29]:


# nota de Pedro
df.loc[11]['Nota']


# In[30]:


# Mostrar solo las columnas (series) indicadas
dfDesdeDict1['Apellido']


# In[31]:


dfDesdeDict1[['Nombre','Apellido']]


# In[32]:


# Nombre y apellido de Ana
dfDesdeDict1[['Nombre','Apellido']].loc[3]  # filtras por serie y buscas la fila con el indice 3
dfDesdeDict1.loc[3][['Nombre','Apellido']]  # primero obtienes la fila y luego filtras por columna


# In[33]:


# Nombre y apellido del elemento que esta en la posicion del indice 4
dfDesdeDict1[['Nombre','Apellido']].iloc[4]


# In[34]:


# Agregar nueva columna al dataframe
resultado = ['Suspenso','Aprobado','Suspenso','Aprobado','Aprobado']
dfDesdeDict1.insert(loc=3, column="Resultado", value=resultado)
dfDesdeDict1


# In[35]:


# Media de los aprobados y suspensos
dfDesdeDict1.groupby(["Resultado"]).mean(["Nota"])


# In[36]:


# Agregar los datos del dfDesdeDict2 al dfDesdeDict1
# Note: pandas.DataFrame.append is deprecated since version 1.4.0 . Rather use concat() .
#dfDesdeDict3 = dfDesdeDict1.append(dfDesdeDict2, ignore_index=True)
# con _append si funciona
dfDesdeDict3 = dfDesdeDict1._append(dfDesdeDict2, ignore_index=True)
dfDesdeDict3


# In[37]:


# Agregar los datos del df_nuevo al dfDesdeDict3
data3 = [[8,'Jorge','Garcia','Suspenso', 4.5], [9,'Maria','Gonzalez','Aprobado',8.9]]
#df_nuevo = pd.DataFrame(data3, columns=['Id','Nombre','Apellido','Resultado','Nota'])
df_nuevo = pd.DataFrame(data3, columns=dfDesdeDict3.columns)
dfDesdeDict3= pd.concat([dfDesdeDict3,df_nuevo], ignore_index=True)
dfDesdeDict3


# In[38]:


# Mostrar cuantos aprobados o suspensos tenemos
#dfDesdeDict3.groupby('Resultado')['Id'].count()
# es lo mismo
print(dfDesdeDict3.groupby(["Resultado"]).size())


# In[39]:


data = {
  'co2': [95, 90, 99, 104, 105, 94, 99, 104],
  'model': ['Citigo', 'Fabia', 'Fiesta', 'Rapid', 'Focus', 'Mondeo', 'Octavia', 'B-Max'],
  'car': ['Skoda', 'Skoda', 'Ford', 'Skoda', 'Ford', 'Ford', 'Skoda', 'Ford']
}

df = pd.DataFrame(data)

print("Media:",df["co2"].mean(), "Max:",df["co2"].max() )


# In[40]:


# Agrupar por apellido y resultado
dfDesdeDict3.groupby(['Apellido','Resultado'])['Id'].count()


# # Tipos de merge:
# # inner:  solo en comun
# # left: todos los de la izquierda + en comun
# # right: todos los de la derecha + en comun
# # outer: todos

# In[41]:


# Preparar los 2 dataframes con un campo en comun
dict1 = [{'Id':1, 'Nombre':'Pantalla', 'Precio':129.50},
         {'Id':2, 'Nombre':'Teclado', 'Precio':49.95},
         {'Id':3, 'Nombre':'Raton', 'Precio':19.75},
         {'Id':4, 'Nombre':'Scanner', 'Precio':300}]
df1 = pd.DataFrame(dict1)

dict2 = [{'Nombre':'Pantalla', 'Proveedor':'Lenovo'},
         {'Nombre':'Teclado', 'Proveedor':'Logitech'},
         {'Nombre':'Raton', 'Proveedor':'Microsoft'},
         {'Nombre':'Impresora', 'Proveedor':'HP'}]
df2 = pd.DataFrame(dict2)
print(df1)
print(df2)


# In[42]:


# merge: inner
df_inner = pd.merge(df1, df2, how='inner', on=['Nombre'])
df_inner


# In[43]:


# merge: left
df_left = pd.merge(df1, df2, how='left', on=['Nombre'])
df_left


# In[44]:


# merge: rigth
df_right = pd.merge(df1, df2, how='right', on=['Nombre'])
df_right

# Es lo mismo
#df_left = pd.merge(df2, df1, how='left', on=['Nombre'])
#df_left


# In[45]:


# merge: outer
df_outer = pd.merge(df1, df2, how='outer', on=['Nombre'])
df_outer


# In[46]:


# Ordenar por columna
pd.merge(df1, df2, how='outer', on=['Nombre']).sort_values('Id',ascending=False)


# In[47]:


# Filtrar por Proveedor HP
df_outer[df_outer['Proveedor'] == 'HP']


# In[48]:


# Mostrar los productos con precio inferior a 100
df_outer[df_outer['Precio'] < 100]


# In[49]:


# Mostrar los productos con mas de 5 caracteres y precio inferor a 100
#df_outer[   (df_outer['Nombre'] == 'Teclado')    &  (df_outer['Precio'] < 100)  ]
df_outer[   (df_outer['Nombre'].str.len() > 5)    &  (df_outer['Precio'] < 100)  ]


# # Borrar:
# # axis = 1 -> eliminar columnas
# # axis = 0 -> eliminar filas

# In[50]:


dfDesdeDict3


# In[51]:


# Si borro una columna, para que el dataframe se actualize hay que hacer una asignacion 
dfDesdeDict3 = dfDesdeDict3.drop('Id', axis=1)
# dfDesdeDict3 = dfDesdeDict3.drop(['Id','Resultado'], axis=1)  # borrar 2 columnas
dfDesdeDict3


# In[52]:


dfDesdeDict3 = dfDesdeDict3.drop(5,axis=0)
dfDesdeDict3


# In[55]:


# Borrar 2 filas, las que tienen el indice 6 y 8
dfDesdeDict3 = dfDesdeDict3.drop([6,8],axis=0)
dfDesdeDict3


# In[56]:


# Borrar por rango de fila
dfDesdeDict3 = dfDesdeDict3.drop(range(0,2),axis=0)  # recordar que el rango, el ultimo no entra
dfDesdeDict3


# In[58]:


# Datos unicos
dfDesdeDict3['Apellido'].unique()
dfDesdeDict3['Apellido'].unique().tolist()


# In[59]:


# Aplicar lambdas
dfDesdeDict3 = dfDesdeDict3['Nota'].apply(lambda n: n+1)
dfDesdeDict3


# In[ ]:


# !pip install pandas


# In[ ]:


# actualiza todo a la ultima version
# pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U
# !pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U


# In[ ]:


get_ipython().system('jupyter --version')


# In[ ]:


# pip install --upgrade pandas


# In[ ]:


# pip list


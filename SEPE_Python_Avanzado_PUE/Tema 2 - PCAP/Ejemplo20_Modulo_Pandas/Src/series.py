#!/usr/bin/env python
# coding: utf-8

# In[ ]:


<h1>Modulo Pandas</h1>


# In[25]:


# importamos el modulo pandas
import pandas as pd


# In[2]:


# crear serie a partir de una lista de nombres
lista = ['Juan', 'Pedro','Estefania','Ana','Esteban']
serie = pd.Series(lista, dtype="string")
serie


# In[11]:


# crear serie a partir de un diccionario
diccionario = {0:'Juan', 1:'Pedro', 2:'Estefania', 3:'Ana', 4:'Esteban'}
diccionario = {key:lista[key] for key in range(len(lista))}
serie = pd.Series(diccionario)
serie


# In[12]:


print('Longitud:',serie.size)


# In[13]:


print('indices de la serie:', serie.index)


# In[14]:


print('Tipo:', serie.dtype)


# In[17]:


# Acceder a los elementos por posicion
print("2 primeros:", serie[:2])  # 2 primeros
serie[:2]


# In[18]:


serie[1:3] # el 3 no esta incluido


# In[19]:


serie[2:]


# In[20]:


# Acceder a los elementos por el indice
serie[0]


# In[22]:


serie[len(serie) - 1]


# In[24]:


serie[[0, 3]]


# In[26]:


# Ejecutar lambdas con apply
serie.apply(lambda nombre: nombre.upper())


# In[ ]:





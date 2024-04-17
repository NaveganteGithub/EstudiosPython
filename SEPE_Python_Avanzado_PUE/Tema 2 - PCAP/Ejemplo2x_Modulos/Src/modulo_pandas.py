#!/usr/bin/env python
# coding: utf-8

# <h1>Modulo Pandas</h1>

# <p>Importar el modulo pandas</p>

# In[1]:


import pandas as pd


# <p>Crear una serie</p>

# In[2]:


lista = ['Juan', 'Pedrio', 'Estefania', 'Ana', 'Esteban']
serie = pd.Series(lista, dtype="string")
serie


# <p>Crear un diccionario</p>

# In[9]:


diccionario = dict([(0,'Juan'), (1,'Pedro'), (2,'Estefania'), (3,'Ana'), (4,'Esteban')])
diccionario = {key:lista[key] for key in range(len(lista))}
serie = pd.Series(diccionario)
diccionario
serie


# In[10]:


print('Longitud:', serie.size)


# In[11]:


print('indices de la serie:', serie.index)


# In[13]:


print('Tipo:', serie.dtype)


# In[14]:


serie[0:3]


# In[15]:


serie[2:]


# In[16]:


serie[0]


# In[17]:


serie[2:]


# In[18]:


serie[len(serie) - 1]


# In[19]:


serie[[0,3]]


# In[20]:


serie.apply(lambda nombre: nombre.upper())


# In[ ]:





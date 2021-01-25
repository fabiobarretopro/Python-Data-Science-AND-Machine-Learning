#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


minha_lista = [1, 2, 3]


# In[5]:


minha_lista


# In[7]:


np.array(minha_lista)


# In[9]:


minha_matrix = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]


# In[11]:


np.array(minha_matrix)


# In[14]:


np.arange(0, 11, 2)


# In[21]:


np.zeros(3)


# In[23]:


arr = np.zeros(3)


# In[25]:


arr


# In[27]:


arr = np.zeros((5, 5))


# In[29]:


arr


# In[34]:


np.ones(3)


# In[37]:


np.ones((3, 3))


# In[39]:


np.eye(5)


# In[41]:


np.linspace(0, 10, 5) #Números igualmente espaçados


# In[43]:


np.random.rand(5) #Sempre entre zero e 1


# In[45]:


np.random.rand(5)*100


# In[48]:


np.random.rand(5, 4)


# In[66]:


np.random.rand(5) #Média zero e desvio padrão 1


# In[65]:


np.random.randint(0, 100, 10) #O último parâmetro é a quantidade de números


# In[68]:


np.random.rand(5)*100


# In[72]:


np.round(np.random.rand(5)*100, 0)#Último parâmetros é a quantidade e casas decimais


# In[74]:


arr = np.random.rand(25) #Cria 25 elementos entre o e 1


# In[76]:


arr


# In[78]:


arr.reshape((5, 5)) #Vira uma matrix de 5 x 5


# In[82]:


arr = arr.reshape((5, 5))


# In[84]:


arr


# In[86]:


arr.shape


# In[88]:


arr.max()


# In[90]:


arr.min()


# In[92]:


arr.argmax() #Índice na qual o maior elemento se encontra.


# In[94]:


arr.argmin() #Índice na qual o menor elemento se encontra.


# In[ ]:





# In[ ]:





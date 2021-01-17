#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[3]:


outside = ["G1", "G1", "G1", "G2", "G2", "G2"]
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)


# In[5]:


outside


# In[7]:


inside


# In[12]:


hier_index = list(zip(outside, inside))


# In[14]:


hier_index


# In[16]:


hier_index = pd.MultiIndex.from_tuples(hier_index)


# In[18]:


hier_index


# In[22]:


df = pd.DataFrame(np.random.randn(6, 2), index=hier_index, columns=["A", "B"])


# In[24]:


df


# In[27]:


df.loc["G1"].loc[1]


# In[29]:


df.index.names = ["Grupo", "Número"]


# In[31]:


df


# In[33]:


df.xs("G1")


# In[35]:


df.xs(1, level="Número")


# In[ ]:





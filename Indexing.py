#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[49]:


df = pd.read_excel(r"C:\Users\HP\Documents\Python doc\world_population_excel_workbook.xlsx",index_col='Country')
df


# In[50]:


df.reset_index(inplace=True)


# In[51]:


df.set_index('Country', inplace =True)
df


# In[52]:


df.loc['Albania']


# In[53]:


df.iloc[1]


# In[54]:


df.reset_index(inplace=True)
df


# In[55]:


df.set_index(['Continent','Country'],inplace=True)


# In[60]:


pd.set_option('display.max.rows',235)


# In[61]:


df.sort_index()


# In[65]:


df.loc['Africa','Angola']


# In[68]:


df.iloc[1]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





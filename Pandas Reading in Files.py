#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv(r"C:\Users\HP\Documents\Python doc\countries of the world.csv")
df


# In[3]:


#df1 = pd.read_csv(r"C:\Users\HP\Documents\Python doc\countries of the world.txt", sep='\t')
#df1
#df1 = pd.read_table(r"C:\Users\HP\Documents\Python doc\countries of the world.csv",sep=',')
#df1

df1 = pd.read_table(r"C:\Users\HP\Documents\Python doc\countries of the world.txt")
df1


# In[11]:


df2 = pd.read_json(r"C:\Users\HP\Documents\Python doc\json_sample.json")
df2


# In[8]:


df3 = pd.read_excel(r"C:\Users\HP\Documents\Python doc\world_population_excel_workbook.xlsx",sheet_name='Sheet1')
df3


# In[10]:


pd.set_option('display.max.rows', 235)
pd.set_option('display.max.columns',40)


# In[12]:


df3.info()


# In[13]:


df3.shape


# In[17]:


df3.head(10)


# In[18]:


df3.tail(10)


# In[20]:


df3['Rank']


# In[21]:


df3.loc[224]


# In[22]:


df3.iloc[224]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





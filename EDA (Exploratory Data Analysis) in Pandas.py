#!/usr/bin/env python
# coding: utf-8

# # EDA (Exploratory Data Analysis) in Pandas

# In[1]:


import pandas as pd
import matplotlib as plt
import seaborn as sns


# In[9]:


df=pd.read_csv(r"C:\Users\HP\Documents\Python doc\world_population.csv")
df
#pd.set_option('display.max.rows',235)


# In[8]:


#in order to remove the 'e' notations in the population we can change the format of float points like shown below...

pd.set_option('display.float_format',lambda x : '%.2f' % x)


# In[12]:


df.info()


# In[13]:


df.describe()


# In[14]:


#In EDA process we need to find the outliers, missing values and things are wrong in the data, etc

df.isnull().sum()


# In[16]:


df.nunique()


# In[24]:


df.sort_values(by ='2022 Population', ascending =False).head(10)


# In[25]:


df.corr()


# In[48]:


sns.heatmap(df.corr(), annot = True)

plt.rcParams['figure.figsize'] = (10,3)


# In[53]:


df.groupby('Continent').mean().sort_values(by='2022 Population',ascending=False)


# In[52]:


df[df['Continent'].str.contains('Oceania')]


# In[74]:


df2 = df.groupby('Continent')[['1970 Population', '1980 Population', '1990 Population',
       '2000 Population', '2010 Population', '2015 Population',
       '2020 Population', '2022 Population']].mean().sort_values(by='2022 Population',ascending=False)
df2


# In[69]:


df.columns[5:13]


# In[ ]:





# In[75]:


df3=df2.transpose()
df3


# In[96]:


df3.plot(figsize=(15,4))
#plt.rcParams['figure.figsize'] = (2,8)


# In[105]:


df.boxplot(figsize=(26,10))


# In[112]:


df.select_dtypes(include='float')


# In[ ]:





# In[ ]:





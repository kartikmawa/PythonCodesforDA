#!/usr/bin/env python
# coding: utf-8

# # Pandas Visualizations 

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[11]:


df =pd.read_csv(r"C:\Users\HP\Documents\Python doc\Ice Cream Ratings.csv", index_col ='Date')
df


# In[65]:


print(plt.style.available)
plt.style.use('seaborn-v0_8-poster')


# In[66]:


df.plot(kind='line', title='Ice Cream Ratings', xlabel='Daily Rating', ylabel='Scores')


# In[63]:


df.plot.barh(stacked= True)


# In[64]:


df.plot.scatter(x='Texture Rating', y='Overall Rating', s=500, c='Red')


# In[40]:


df.plot.hist(bins=100)


# In[43]:


#min->25->50->75->max
df.boxplot()


# In[52]:


df.plot.area(figsize=(10,5))


# In[56]:


df.plot.pie(y='Flavor Rating', figsize=(10,6))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# #    Data cleaning in Pandas

# In[1]:


import pandas as pd


# In[17]:


df=pd.read_excel(r"C:\Users\HP\Documents\Python doc\Customer Call List.xlsx")
df


# In[18]:


df=df.drop_duplicates()


# In[19]:


df


# In[20]:


df.drop(columns='Not_Useful_Column', inplace=True)


# # Cleaning using strip----> For last name

# In[25]:


#df['Last_Name']=df['Last_Name'].str.lstrip('...')
#df['Last_Name']=df['Last_Name'].str.lstrip('/')
#df['Last_Name']=df['Last_Name'].str.rstrip('_')

df['Last_Name']=df['Last_Name'].str.strip('123._/')


# # Standardising the phone numbers

# In[40]:


#df['Phone_Number']=df['Phone_Number'].str.replace('[^a-zA-Z0-9]','')
#df['Phone_Number']=df['Phone_Number'].apply(lambda x : str(x))
#df['Phone_Number']=df['Phone_Number'].apply(lambda x: x[0:3]+'-'+x[3:6]+'-'+x[6:10])
#df['Phone_Number']=df['Phone_Number'].str.replace('nan--','')
#df['Phone_Number']=df['Phone_Number'].str.replace('Na--','')
df


# # Splitting the Address into 3 columns

# In[47]:


df[['Street_Address','State','Zip_Code']]=df['Address'].str.split(',',2, expand=True)
df


# In[53]:


df['Do_Not_Contact']=df['Do_Not_Contact'].str.replace('Yes','Y')
df['Do_Not_Contact']=df['Do_Not_Contact'].str.replace('No','N')
df


# In[64]:


#df=df.replace('N/a','')
#df=df.fillna('')
df


# In[66]:


for x in df.index:
    if df.loc[x,'Do_Not_Contact']=='Y':
        df.drop(x,inplace=True)
df


# In[73]:


for x in df.index:
    if df.loc[x,'Phone_Number']=='':
        df.drop(x,inplace=True)
df

#another way to clean blank data
#df.dropna(subset='Phone_Number',inplace=True)


# In[70]:


df.reset_index(drop=True)
df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





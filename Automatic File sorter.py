#!/usr/bin/env python
# coding: utf-8

# # Automatic File Sorter in File Explorer

# In[45]:


#OS is Operating sys and shutil will allow us to do high operations in file exp

import os, shutil


# In[46]:


path =r"C:/Users/HP/Documents/Py pto/"


# In[47]:


file_names= os.listdir(path)
print(file_names)


# In[48]:


folder_names = ['csv files', 'image files', 'text files']
for loop in range(0,3):
    if not os.path.exists(path + folder_names[loop]):
        os.makedirs((path + folder_names[loop]))

for file in file_names:
    if ".xlsx" in file or ".docx" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file)
    elif ".jpg" in file or ".png" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".txt" in file and not os.path.exists(path + "text files/" + file):
        shutil.move(path + file, path + "text files/" + file)
    else:
        print('There are files in this path that were not moved')


# In[40]:





# In[ ]:





# In[ ]:





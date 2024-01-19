#!/usr/bin/env python
# coding: utf-8

# # Beautiful Soups and Requests

# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


url = "https://www.scrapethissite.com/pages/forms/"


# In[6]:


page = requests.get(url)


# In[9]:


soup = BeautifulSoup(page.text, 'html')


# In[10]:


print(soup)


# In[11]:


print(soup.prettify())


# In[ ]:





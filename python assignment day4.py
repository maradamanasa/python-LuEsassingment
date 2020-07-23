#!/usr/bin/env python
# coding: utf-8

# In[9]:


str1="what we think we become;we are python programmers"
res=str1.count("we")
print(res)


# In[10]:


str1.find("we")


# In[11]:


str1.rfind("we")


# In[14]:


str2="we"
for i in range(1,len(str1.split())):
    if str1.find(str2):
        print(str1.find(str2))
        


# In[ ]:





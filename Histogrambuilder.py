
# coding: utf-8

# In[1]:


import pandas as pd #Importing pandas package


# In[2]:


df=pd.read_excel("try.xlsx") #WE are importing the excel file-mention the exact directory


# In[3]:


df


# In[4]:


df.sort_values('x2') #Sorting values of x2 


# In[5]:


data_h=df['x2']


# In[9]:


data_h=data_h.fillna(0) #Replacing all NaN to 0


# In[7]:


import matplotlib.pyplot as plt


# In[10]:


plt.hist(data_h,bins=20) #Histogram formed out of data and bin values can be set with bins=[10,20,....] and range is automatic to min and max values of data


# In[11]:


plt.show()


# In[13]:


plt.savefig("C:\Users\Administrator\Desktop\hist1.png") #give the directory to save image


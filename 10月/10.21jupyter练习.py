#!/usr/bin/env python
# coding: utf-8

# #输入数组

# In[3]:


import numpy as np
s=np.array([[56.0,0.0,4.4,68.0],
          [1.2,104.0,52.0,8.0],
          [1.8,135.0,99.0,0.9]])
print(s)


# #计算每列的和
# #不要使用秩为1的数组。例如：s=np.random.randn(5) 错误写法

# In[7]:


s1=s.sum(axis=0)
print(s1)


# #计算出每列各数字的占比

# In[8]:


end=100*s/s1
print(end)


# In[12]:


s=np.random.randn(1,5)
print(s)
s1=np.random.randn(5,1)
print(s1)


# In[11]:


print(s.shape)


# #数组可以使用reshape修改

# In[15]:


s3=np.random.randn(5)
s3=s3.reshape(5,1)
print(s3)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# #这是一号标题

# In[5]:


import numpy as np
a=np.array([1,2,3,4])
print(a)


# $E=mc^2$

# In[18]:


import time

a=np.random.rand(1000000)
b=np.random.rand(1000000)

tic=time.time()
c=np.dot(a,b)
toc=time.time()
print(c)
print("向量化:"+str(1000*(toc-tic))+'ms')

c=0
tic=time.time()
for i in range(1000000):
    c+=a[i]*b[i]
toc=time.time()
print(c)
print("非向量化:"+str(1000*(toc-tic))+'ms')


# In[ ]:





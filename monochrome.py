#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt
from skimage import data
photo_data = misc.imread("farm1.png")
x,y,z=photo_data.shape  
photo_data[:] = photo_data.mean(axis=-1,keepdims=1) 
plt.figure(figsize=(10,10))
plt.imshow(photo_data)


# In[ ]:





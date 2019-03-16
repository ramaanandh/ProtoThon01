#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
a=input("Enter the input separated by comma")
b=a.split(',')
n=len(b)
sum=0
sqrt=0
for i in b:
    sum+=float(i)
avg=(sum/n)
s=math.sqrt(avg)
print("The root mean square of the input numbers is",s)


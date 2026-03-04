#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

Func = input("Give function, x for example: ")
# Get user input for limits
a = float(input("Give the lower limit: "))
b = float(input("Give the higher limit: "))

#Make a uniform list
x = np.random.uniform(0,1,10000)

def Int(func, a, b):
    Int = (b-a)/len(x)*np.sum(eval(Func))
    return(Int)

print(f"{Int(Func,a,b):.2f}")


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


masses = [1.9891e+30, 1.8986e+27, 
          5.6846e+26, 1.0243e+26, 8.6810e+25,
          5.9736e+24, 4.8685e+24, 6.4185e+23, 
          3.3022e+23, 7.349e+22, 1.25e22]
moon = masses[9]
NewMasses = [] #Create Empty placeholderlist
for i in range(len(masses)):
    if masses[i] > moon:
        NewMasses.append(masses[i])
print(f"New list: {NewMasses} with lenght: {len(NewMasses)}")
FirstFive = masses[slice(5)]
AVG = sum(FirstFive)/len(FirstFive)
print(f"First 5 masses from the orignal list: {FirstFive}, with average mass = {AVG}")


# In[ ]:





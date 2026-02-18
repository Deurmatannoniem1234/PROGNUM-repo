#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Define Variables
D=float(input("What day is it?"))
M=int(input("What Month is it?(1,2,3,4 etc):"))
Y=int(input("What Year is it?(From 1582 and onwards):"))
#Calculate
JD = 367*Y -7*(Y+(M+9)//12)//4 - 3*((Y+(M-9)//7)//100 + 1)//4 + (275*M)//9 + D + 1721029-0.5
#Print
print(f"The Julian Date is: {JD} Days")


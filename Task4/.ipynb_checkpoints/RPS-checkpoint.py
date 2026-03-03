#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

RPS = input("Rock, paper or Scissor? (give R, P or S)")
Comp = np.random.randint(1,4) #Generate the Computer Awnser

#Convert Awnser to number Rock = 1, Paper = 2, Scissor = 3
if RPS == "R":
    RPS = 1
elif RPS == "P":
    RPS = 2
elif RPS == "S":
    RPS = 3
else:
    print("That is not R, P or S")
    
#Who Won?
if RPS == Comp:
    print(f"you tied!")
elif RPS - Comp == 1 or RPS == 1 and Comp == 3:
    print(f"You Won!")
elif Comp - RPS == 1 or Comp == 1 and RPS == 3:
    print(f"You Lost :(")


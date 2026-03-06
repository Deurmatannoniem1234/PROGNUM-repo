#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from IPython.display import display, Latex

Func = lambda x: A*np.exp(-(x-x0)**2/(2*sig**2))+z0

def gauss(x, A, x0, sigma, z0):
    return A*np.exp(-(x-x0)**2/(2*sigma**2))+z0

A = float(input("Give the value of the Amplitude, for example  1.0"))
x0 = float(input("Give the position of the peak, for example  0.0"))
sig = float(input("Give the width of the peak, for example  2.0"))
z0 = float(input("Give the ofset to the x axis, for example  0.0"))

x = np.linspace(-10,10,200)
y = gauss(x, A, x0, sig, z0)

print(f"the area between x = 0 and x = 2.5: {sp.integrate.quad(Func, 0, 2.5)[0]}")


display(Latex(rf"the area to infinity is: {sp.integrate.quad(Func, -np.inf, np.inf)[0]:.2f} which is the same as the formula given from the integral $A\sigma\cdot\sqrt{{2\pi}}$ = {A*sig*sqrt(2*np.pi):.2f}"))

mask = (x>0) & (x<2.5)

plt.plot(x,y)
plt.fill_between(x[mask], y[mask], 0, alpha = 0.4, color = "red", label = round(sp.integrate.quad(Func, 0, 2.5)[0],2))
plt.legend()
plt.show()


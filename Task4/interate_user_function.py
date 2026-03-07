#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from numpy import sin, cos, tan, exp, pi
from scipy.integrate import quad
import sympy as sp
from IPython.display import display, Latex

a = 0
b = np.pi

def MCI(func_str, a, b):
    x_samples = np.random.uniform(a, b, 100000)
    try:
        # Evaluate at every point
        y_values = eval(func_str, {"x": x_samples, "sin": sin, "cos": cos, "tan" : tan, "exp": exp, "pi": pi})
        return (b - a) * np.mean(y_values)
    except Exception as e:
        raise e
display(Latex(r"The following is a integration tool that integrates from 0 to $\pi$."))
display(Latex(r"Enter a function of x (e.g., x**4 + exp(sin(x) + cos(x))): "))
              
func_input = input()
    
try:
    # 1. SciPy quad Integration
    # Define a wrapper for quad that uses eval
    f_eval = lambda x: eval(func_input, {"x": x, "sin": sin, "cos": cos, "exp": exp, "pi": pi})
    quad_result = quad(f_eval, a, b)[0]
        
    # 2. MCI
    mc_result = MCI(func_input, a, b)
     
    print(f"\nResults for integral from 0 to pi:")
    print(f"SciPy quad(): {quad_result:.6f}")
    print(f"Monte Carlo:  {mc_result:.6f}")
    print(f"Difference:   {abs(quad_result - mc_result):.6e}")

except NameError as e:
    print(f"Error: Variable or function not recognized. {e}")
except SyntaxError:
    print(f"Error: Invalid syntax in your expression. Please check your parentheses and operators.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


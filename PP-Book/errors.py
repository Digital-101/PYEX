# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 08:26:49 2024

@author: mk9di
"""

try:
    10 * (1/0)
except:
    print("The calculation failed")
    
x = 2

try:
    print(x)
except NameError:
    print("x is not defined")
except:
    print("Something is wrong")
finally:
    print("The program is finished")

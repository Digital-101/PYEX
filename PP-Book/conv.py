# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 08:00:46 2024

@author: mk9di
"""

from fahrenheit import c2f, f2c

Tc = 0
Tf = c2f(Tc)

print("Fahrenheit: "+ str(Tf))

Tf = 32
Tc = f2c(Tf)

print("Celsius: "+ str(Tc))
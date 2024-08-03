# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 09:10:02 2024

@author: mk9di
"""

#0
fn = 10
fib1 = 0
fib2 = 1

print(fib1)
print(fib2)

for f in range(fn-2):
    fib_next = fib2 + fib1
    fib1 = fib2
    fib2 = fib_next
    print(fib_next)
    
#1 
n = 10
fib0 = [0, 1]

for h in range(n-2):
    fib_next = fib0[h+1] + fib0[h]
    fib0.append(fib_next)
print(fib0)    

#2 - using numpy
import numpy as np

N = 10

fib = np.zeros(N)

fib[0] = 0
fib[1] = 1

for k in range(N-2):
    fib[k+2] = fib[k+1] + fib[k]

print(fib)
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 18:18:24 2024

@author: mk9di
"""


def stat(x):
    totalsum = 0
    for x in data:
        totalsum += x
        
    N = len(data)
    
    mean = totalsum / N
    
    return totalsum, mean

data = [1,5,6,3,12,3]

totalsum, mean = stat(data)

print(totalsum, mean)
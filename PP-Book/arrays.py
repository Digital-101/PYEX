# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 15:53:37 2024

@author: mk9di
"""

data = [1.6, 3.4, 5.5, 9.4]

N = len(data)
print(N)

data.append(11.4)

N = len(data)
print(N)

for x in data:
    print(x)

carlist = ["Volvo", "Tesla", "Ford"]
for car in carlist:
    print(car)
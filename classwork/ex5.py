# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 13:32:23 2024

@author: dop24
"""
#1 print numbers
for i in range(10,0,-1):
    print(i)
 
#2 multiples of 2
j = 2
while j <= 20:
    print(j)
    j += 2
    
#3 divisible by 3
k = 1
while k <= 100:
    if k % 3 == 0:
        print(k)
    k += 1
    
#4 counting down
l = 100
while l >= 1:
    print(l)
    l -= 5
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 09:46:16 2024

@author: dop24
"""

#1. print even numbers from 1 to 100
m = 1
while m <= 100:
    m+=1
    if m % 2 == 0:
        print(m)
        
#or
i = 2
while i <= 100:
    print(i)
    i+=2
        
#2. Indexing is important
scores = [85, 92, 78, 95, 88, 76, 95]
n = 0
while n < len(scores):
    if scores[n] > 80:
        print(scores[n])
    n+=1
        
  
#3. Print all even numbers from the list numbers
numbers = [1,2,3,4,5,6,7,8,9,10]
o = 0
while o < len(numbers):
    if numbers[o] % 2 == 0:
        print(numbers[o])
    o+=1

    
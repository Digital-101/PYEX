# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 11:58:42 2024

@author: dop24
"""


# Comments

#This is a single line

fruits = ["apple", "banana", "orange", "mango"]
fruits.append("peach")

fruits.pop(0)

for fruit in fruits:
    print(fruit)

"""This is a Multiline comment"""

for i in range(1, 21):
    if i % 3 == 0:    
        print(i)
        
#print numbers 1-5
v = 0 
while v < 5:
    v += 1
    print(v)
    
cars = ['vw', 'toyota', 'mahindra', 'subaru']
i = 0
while i < len(cars):
    print(cars[i])
    i+=1

numbers = [48, 67, 32, 44, 69, 84]
j = 0
while j < len(numbers):
    print(numbers[j])
    j = j + 1

#print numbers from 1-10
k = 1
while k <= 10:
    print(k)
    k+=1
    
#print numbers from 20-3
l = 20
while l >= 3:
    print(l)
    l-=1




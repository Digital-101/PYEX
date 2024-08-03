# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 07:57:48 2024

@author: dop24
"""
#i)
strings = ["Systems Development", "Hello, World", "Cascading Style Sheets", "Hypertext Markup Language"]
for i in strings:
    print(i)

#ii)
style = strings[2]
print(style[2:6])

#iii)
html = len(strings[3])
print(html)



hello = "Hello"
for j in range(5):
    print(hello)
    

string = "Cascading Style Sheets"
#print(string[2:])

#Indexing is important always remember
for m in range(3,len(string)):
    char = string[m]
    sliced = string[m:m+1]
    print(f"{sliced}")

for k in range(35, 61,5):
    print(k)
    
for l in range(-28, 2, 3):
    print(l)
    
cars = ["cherry", "Toyota", "Audi", "Fiat"]
for car in cars:
    print(car)
    
personal_details = ["Nicky","Masiya","February",1990]
personal_details.pop(3)
for p in personal_details:
    print(p)
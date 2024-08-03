# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 09:43:11 2024

@author: dop24
"""

a = [8, 4, 16, 32, 31, 39]

#1 Access the 4th, 5th and the last element
print(a[3])
print(a[4])
print(a[-1])

#2 Add [25, 96, 30] to the data structure above
a.append(25)
a.append(96)
a.append(30)
print(a)

#3 Delete 1st and 2nd elements
del a[0]
del a[0]
print(a)
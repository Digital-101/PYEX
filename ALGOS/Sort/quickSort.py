# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 14:28:12 2024

@author: mk9di
"""

#Quick Sort
my_list = [20, 14, 25, 16, 45, 60, 12, 9]
def Quick_sort(a):
    if len(a) < 2:
        return a
    
    pos = 0
    for i in range(1, len(a)):
        if a[i] <= a[0]:
            pos = pos + 1
            temp = a[i]
            a[i] = a[pos]
            a[pos] = temp
            
    temp = a[0]
    a[0] = a[pos]
    a[pos] = temp
    
    left = Quick_sort(a[0:pos])
    right = Quick_sort(a[pos+1:len(a)])
    
    sorted_array = left + [a[pos]] + right
    
    return sorted_array

Quick_sort(my_list)
print(Quick_sort(my_list))
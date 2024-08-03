# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 14:11:03 2024

@author: mk9di
"""

#Bubble sort
import numpy as np
my_array = np.array([20,14,25,16,45,60,12,9])
def bub_sort(array):
    for i in range(0, len(array)):
        for j in range(0, len(array) - i -1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1]=temp
    return array

bub_sort(my_array)
print(bub_sort(my_array))

print()

#Selection Sort
def sel_sort(array):
    for i in range(len(array)):
        min_elem = i
        for j in range(i+1, len (array)):
            if array[j] < array[min_elem]:
                min_elem = j
                temp = array[i]
                array[i] = array[min_elem]
                array[min_elem] = temp
    return array

sel_sort(my_array)
print(sel_sort(my_array))
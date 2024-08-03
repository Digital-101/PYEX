# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 14:40:24 2024

@author: mk9di
"""

#Inserton Sort
my_list = [20, 14, 25, 16, 45, 60, 12, 9]
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j - 1] = array[j]
            array[j] = key
            j -= 1
            
    return array

insertion_sort(my_list)
print(insertion_sort(my_list))
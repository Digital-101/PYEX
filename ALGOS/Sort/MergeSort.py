# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 14:57:39 2024

@author: mk9di
"""

#Merge Sort
def merge_sort(array):
    if len(array) > 1:
        left = array[:len(array)//2]
        right = array[len(array)//2:]
        merge_sort(left)
        merge_sort(right)
        i,j,k = 0,0,0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[k] = left[i]
                i = i+1
            else:
                array[k] = right[j]
                j = j+1
            k = k + 1
        
        while i < len(left):
            array[k] = left[i]
            i = i + 1
            k = k + 1
            
        while j < len(right):
            array[k] = right[j]
            j = j + 1
            k = k + 1
            
    return array

my_list = [20, 14, 25, 16, 45, 60, 12, 9]
merge_sort(my_list)
print(merge_sort(my_list))
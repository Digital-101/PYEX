# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 14:50:45 2024

@author: mk9di
"""

#binary search
def binary_search(array, elem):
    low = 0
    high = len(array) - 1
    Temp = False
    
    while (low <= high and not Temp):
        mid = (low + high) // 2
        if array[mid] == elem:
            Temp = True
        else:
            if elem < array[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return Temp

my_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
binary_search(my_array, 3)
print(binary_search(my_array, 23))
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 14:45:07 2024

@author: mk9di
"""

#Linear Search
def search(array, x):
    for i in range(0, len(array)):
        if array[i] == x:
            return True
     
my_list = [20, 14, 25, 16, 45, 60, 12, 9]
#search(my_list, 9)
print(search(my_list, 16))
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 19:37:34 2024

@author: mk9di
"""

list1 = [1, 2, 3, 4, 5, 6]

list2 = [7, 8, 9, 10]

#list1.append(list2)
#list1.insert(list2)
list1.extend(list2)

print(list1)

import calendar
yy = 2025
mm = 1
print(calendar.month(yy, mm))
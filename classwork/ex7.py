# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 09:46:38 2024

@author: dop24
"""

address = [100, "Neptune", "Riet river", "road", "Verulam"]

#access
print(address[0])

#delete 
address.pop(3)

#extend
address.append("Drive")

for i in address:
    print(i)

j = 1

while j <= 10:
    print(j)
    j+=1 
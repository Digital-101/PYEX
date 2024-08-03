# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 08:15:18 2024

@author: mk9di
"""

f = open("file.docx", "x")
data = "Hello Python"
f.write(data)
f.close() 

f = open("file.txt", "r")
data = f.read()
print(data)
f.close()       
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 20:39:51 2024

@author: mk9di
"""
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
    # 100 even numbers
    for i in range(1,101):
        if i % 2 == 0:
            print(i, end=" ")
else:
    print("Odd")
    # 100 odd numbers
    for i in range(1,101):
        if i % 2 != 0:
            print(i, end=" ")


# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 11:12:03 2024

@author: mk9di
"""

#SelfCheckout

total = 0 

for i in range(1,4):
    item = float(input(f"Enter the price of item {i}: "))
    quantity = float(input(f"Enter the quantity of item {i}: "))
    
    item *= quantity
    total += item
    
    subtotal = total
    tax = subtotal * (5.5/100)
    Total = subtotal + tax
    
print()
print(f"Subtotal: R{subtotal}")
print(f"Tax: R{tax}")
print(f"Total: R{Total}")
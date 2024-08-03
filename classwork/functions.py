# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 11:15:00 2024

@author: dop24
"""

#functions in python


def greet(name):
    return f"Hello, {name}!"

#call the function
greet("Digits")

#Positional arguments and keyword arguments.
def calculate(x, y, operation='add'):
    if operation == 'add':
        return x + y
    elif operation == 'subtract':
        return x - y
    # more operations...


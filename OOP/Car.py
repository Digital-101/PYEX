# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 13:57:39 2024

@author: mk9di
"""

class Car:
    
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    
    def drive(self):
        print("This "+self.model+" is driving.")
        
    def stop(self):
        print("This car is stoping.")
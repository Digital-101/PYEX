# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 10:29:29 2024

@author: mk9di
"""
#Love Calculator
import random
import math

name1 = input("Enter your name: ")
name2 = input("Enter his/her name: ")

loveScore = random.randint(1, 100)
lovescore = math.floor(loveScore) + 1

print()

if loveScore > 70:
    print("Your lovescore is "+str(loveScore)+"% \nYou both love yourselves like God loves Man.")
elif loveScore > 30 and loveScore <= 70:
    print("Your lovescore is "+str(loveScore)+"%")
elif loveScore <= 30:
    print("Your lovescore is "+str(loveScore)+"% \nYou both love yourselves like oil and water.")
else:
    print("Your lovescore is "+str(loveScore)+"%")
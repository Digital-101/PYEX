# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 10:36:47 2024

@author: dop24
"""

#Dictionary data structure to store driving ages by countries in the African continent.
countries = {
        16: ["Cameroon", "Senegal", "Zimbabwe", "Zambia"],
        17: ["Mozambique", "South Africa"],
        18: ['Algeria', 'Eswatini', 'Kenya', 'Ethiopia', 'Kenya', 'Lesotho','Libya','Mali','Mauritania',
             'Mauritius','Mauritius','Mayotte','Morocco','Namibia','Niger','Nigeria','Reunion','Rwanda',
             'Tanzania','Tunisia','Uganda']
        }  

try:
    age = int(input("What is your age: "))

    #Constraints
    message = "You are old enough to legally drive." if age >= 16 else 'You are not old enough to legally drive.'
    print(message)
    
    #Challenges
    if age < 0:
        print("Error... Age must be a whole number")
    elif age == 16:
        print(f"You can legally drive in: {countries[16]} ")
    elif age == 17:
        print(f"You can legally drive in: {countries[17]} ")
    elif age > 17:
        print(f"You can legally drive in: {countries[18]} ")
        
except ValueError:
    print("Error... Enter valid age!")
    

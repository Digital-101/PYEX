# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 19:55:54 2024

@author: mk9di
"""

from datetime import datetime

#prompt user
name = input("Enter your name: ")
dob = input("Enter your date-of-birth in the form -> (YYYY-MM-DD): ")

#function to calculate days lived
def calculate_days_lived(dob):
    #using strptime() to get date format yyyy-mm-dd
    dob = datetime.strptime((dob), '%Y-%m-%d')
    #get today() and minus days from dob
    today = datetime.now()
    days_lived = (today - dob).days
    return days_lived

#calling calculate_days_lived function
days_lived = calculate_days_lived(dob)
#displaying name and days lived
print(f"{name} has lived approcimately {days_lived} days.")
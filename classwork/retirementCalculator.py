# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 08:07:20 2024

@author: dop24
"""

import datetime

age = int(input("What is your current age? "))
retireAge = int(input("At what age would you like to retire? "))

currentYear = datetime.datetime.now().year
yearDiff = retireAge - age
retireYear = currentYear + yearDiff

print(f"You have {yearDiff} years left until you can retire.")
print(f"It's {currentYear}, so you can retire in {retireYear}.")
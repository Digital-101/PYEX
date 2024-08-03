# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 14:01:57 2024

@author: mk9di
"""

from Car import Car

car_1 = Car("VW", "Golf 7", 2019, "Blue")

car_2 = Car("Ford", "Mustand", 2023, "Yellow")

print(car_1.make)
car_1.stop()
print()
car_2.drive()
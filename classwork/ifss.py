# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 10:47:50 2024

@author: dop24
"""

x = 85

if x > 80:
    print("A")
elif x < 40:
    print("F")
    
age = int(input("Enter your age: "))
if age >= 18:
    print("Adult")
else:
    print('Minor')
    
weather = input('Enter weather forecast: ')

if weather == 'sunny':
    print("Go outside and play")
elif weather == 'rainy':
    print("Stay inside and read a book")
else:
    print('Check the forecast agin')
    
import datetime

dt = datetime.datetime.now()
day = dt.strftime('%A')
print("Today is "+day)
if day == 'Monday':
    print("Start of week")
elif day == 'Friday':
    print('Almost Weekend')
else:
    print('Just Another day')
    
temp = int(input("Enter temperatute: "))
if temp >= 25:
    print('Hot Weather')
elif temp > 15 and temp < 25:
    print('Mild Weather')
else:
    print('cold weather')

score = int(input("Enter your score: "))
if score >= 90:
    print('A')
elif score > 80 and score < 89:
    print('B')
elif score > 70 and score < 79:
    print('C')
elif score > 60 and score < 69:
    print('D')
else:
    print('F')
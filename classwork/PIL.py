# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 21:32:44 2024

@author: mk9di
"""

from PIL import Image
Image.open('wolf.jpg')
import pywhatkit
pywhatkit.image_to_ascii_art('wolf.jpg','MyArt')
read_file = open("MyArt.txt", "r")
print(read_file.read())
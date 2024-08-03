# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 15:26:18 2024

@author: mk9di
"""

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

y = [5, 2, 4, 4, 8, 7, 4, 8, 10, 9]

plt.plot(x,y)
plt.xlable("Time (s)")
plt.ylabel("Temperature (degC)")
plt.show()
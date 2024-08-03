# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 08:54:18 2024

@author: mk9di
"""

import statistics as st

data = [-1.0, 2.5, 3.25, 5.75]

#Mean or Average
m = st.mean(data)
print(m)

#Standard Deviation
st_dev = st.stdev(data)
print(st_dev)

#Median
med = st.median(data)
print(med)

#Variance
var = st.variance(data)
print(var)
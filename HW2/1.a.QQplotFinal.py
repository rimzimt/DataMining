#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 13:34:05 2019

@author: rimzimthube
"""

import numpy as np
import statsmodels.api as sm
from matplotlib import pyplot as plt


#Section A grades
x=np.array([47, 63, 71, 39, 47, 49, 43, 37, 81, 69, 38, 13, 29, 61, 49, 53, 57, 23, 58, 17, 73, 33, 29])

#Section B grades
y=np.array([20, 49, 85, 17, 33, 62, 93, 64, 37, 81, 22, 18, 45, 42, 14, 39, 67, 47, 53, 73, 58, 84, 21])

pp_x = sm.ProbPlot(x, fit=True)
pp_y = sm.ProbPlot(y, fit=True)

# QQ plot for Section A and B 
fig = pp_x.qqplot(other=pp_y, line='45')

plt.xlabel('Section A')
plt.ylabel('Section B')
plt.show()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 13:07:03 2019

@author: rimzimthube
"""

import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns



train=pd.read_csv('/Users/rimzimthube/MS/Data Mining/HW3/titanic_train.csv')
test=pd.read_csv('/Users/rimzimthube/MS/Data Mining/HW3/titanic_test.csv')

corr=train.corr()
#corr.style.background_gradient(cmap='coolwarm')
plt.subplots(figsize=(10, 5))
snsheatmap=sns.heatmap(corr, vmax=.9, square=True,annot=True)
#snsheatmap.savefig('/Users/rimzimthube/MS/Data Mining/HW3/VisualizationOutput/TitanicHeatMap.png')
#plt.show()

plt.subplots(figsize=(10, 5))
snspairplot=sns.pairplot(train,hue="Survived")
plt.show()
snspairplot.savefig('/Users/rimzimthube/MS/Data Mining/HW3/VisualizationOutput/TitanicPairPlot.png')


g = sns.swarmplot(y = "Pclass",
              x = 'Age', 
              data = train,
              # Decrease the size of the points to avoid crowding 
              size = 7)
g.savefig('/Users/rimzimthube/MS/Data Mining/HW3/VisualizationOutput/TitanicSwarmPlot.png')



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 20:57:21 2019

@author: rimzimthube
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

wine_dataset=pd.read_csv('/Users/rimzimthube/MS/Data Mining/HW4/wine.data',header=None)

#Read the dataset
print(wine_dataset.head)

#print(wine_dataset[0])

wine_dataset.to_csv('/Users/rimzimthube/MS/Data Mining/HW4/column.csv')

df_alcohol=pd.DataFrame({'Alcohol':wine_dataset[1] })

# Binning based on equal interval
df_alcohol['bins']=pd.cut(df_alcohol['Alcohol'],4,labels=["A","B","C","D"])
#print('Bins of Alcohol column')
#print(df_alcohol['bins'])

print('Binning of Alcohol column in A, B, C, D bins')
print(df_alcohol)

#Binning based on user defined intervals
df_malic=pd.DataFrame({'MalicAcid':wine_dataset[2]})

bins=[1,2,3,4,5,6]
df_malic['bins']=pd.cut(df_malic['MalicAcid'],bins)
print('Bins of Malic Acid column in 1, 2, 3, 4, 5, 6 columns')
print(df_malic)

#Sampling 
# Take only 75% of the dataset
print('\n Sampling only 75% of the data')
print('Size of the dataset before sampling')
print(wine_dataset.shape)
rows = wine_dataset.sample(frac =.75) 
print('Size of the dataset after sampling')
print(rows.shape)






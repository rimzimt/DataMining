#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 13:36:07 2019

@author: rimzimthube
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from kmodes.kmodes import KModes


wine_dataset=pd.read_csv('/Users/rimzimthube/MS/Data Mining/HW4/wine.data',header=None)

km = KMeans(
    n_clusters=3, init='random',
    n_init=10, max_iter=300, 
    tol=1e-04, random_state=0
)

y_km = km.fit_predict(wine_dataset)

print(y_km)

kmMode = KModes(n_clusters=3, init='random', n_init=10, verbose=1)

y_kmode=kmMode.fit_predict(wine_dataset)
print('kmode')
print(y_kmode)


df=pd.DataFrame({'one': y_km})
df['two']=pd.DataFrame({'two': y_kmode})

print(df)
df.to_csv('/Users/rimzimthube/MS/Data Mining/HW4/mode.csv')



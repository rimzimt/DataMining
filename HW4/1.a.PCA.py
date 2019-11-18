#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 00:29:43 2019

@author: rimzimthube
"""

'''
HW4 Problem 1.a.
'''
# %% libraries

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt


# %% Read the CSV 

wine_dataset=pd.read_csv('/Users/rimzimthube/MS/Data Mining/HW4/wine.data',header=None)

#Read the dataset
#print(wine_dataset.head())

# %% Data Preprocessing

#Separate the data and class label values
X,y=wine_dataset.iloc[:,1:].values, wine_dataset.iloc[:, 0].values

#Separate the training and test data
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,stratify=y, random_state=0)

#Standarise the features
StdScalar=StandardScaler()
X_train_standard=StdScalar.fit_transform(X_train)
X_test_standard=StdScalar.fit_transform(X_test)

# %% PCA steps

#Calculate the covariance matrix
covariance_matrix=np.cov(X_train_standard.T)

#Find the Eigen values and vectors
eigen_values, eigen_vectors=np.linalg.eig(covariance_matrix)


# %% Plot the Eigen vectors

variance=[]
# Calculate cumulative sum of explained variances
tot = sum(eigen_values)

for value in sorted(eigen_values,reverse=True):
    variance.append(value/tot)

# plot explained variances
plt.bar(range(1,14), variance, alpha=0.5,
        align='center')
plt.ylabel('Variance ratio')
plt.xlabel('Principal components')
plt.legend(loc='best')
plt.show()







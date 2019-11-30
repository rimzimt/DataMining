#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 16:35:22 2019

@author: rimzimthube
"""

#imports
import numpy as np
import pandas as pd
import math

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt
import seaborn as sns

#import training dataset
train_df = pd.read_csv('/Users/rimzimthube/MS/Data Mining/HWExtraCredit/student/student-mat.csv')

#see the columns in our data
#train_df.info()

# take a look at the head of the dataset
print(train_df.dtypes)

#create our X and y


train_df['sex']=train_df['sex'].astype('category').cat.codes
train_df['school']=train_df['school'].astype('category').cat.codes
train_df['address']=train_df['address'].astype('category').cat.codes
train_df['famsize']=train_df['famsize'].astype('category').cat.codes
train_df['Pstatus']=train_df['Pstatus'].astype('category').cat.codes
train_df['Mjob']=train_df['Mjob'].astype('category').cat.codes
train_df['Fjob']=train_df['Fjob'].astype('category').cat.codes
train_df['reason']=train_df['reason'].astype('category').cat.codes
train_df['guardian']=train_df['guardian'].astype('category').cat.codes
train_df['schoolsup']=train_df['schoolsup'].astype('category').cat.codes
train_df['famsup']=train_df['famsup'].astype('category').cat.codes
train_df['paid']=train_df['paid'].astype('category').cat.codes
train_df['activities']=train_df['activities'].astype('category').cat.codes
train_df['nursery']=train_df['nursery'].astype('category').cat.codes
train_df['higher']=train_df['higher'].astype('category').cat.codes
train_df['internet']=train_df['internet'].astype('category').cat.codes
train_df['romantic']=train_df['romantic'].astype('category').cat.codes

X = train_df.drop('G3',axis=1)
y = train_df['G3']

print(train_df.head())

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.3)
#
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

print('Training score: {}'.format(lr_model.score(X_train, y_train)))
print('Test score: {}'.format(lr_model.score(X_test, y_test)))

y_pred = lr_model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
rmse = math.sqrt(mse)

print('RMSE: {}'.format(rmse))

steps = [
    ('scalar', StandardScaler()),
    ('poly', PolynomialFeatures(degree=2)),
    ('model', LinearRegression())
]

pipeline = Pipeline(steps)

pipeline.fit(X_train, y_train)
print('\n Linear Regression')
print('Training score: {}'.format(pipeline.score(X_train, y_train)))
print('Test score: {}'.format(pipeline.score(X_test, y_test)))
y_pred = pipeline.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
rmse = math.sqrt(mse)

print('RMSE: {}'.format(rmse))

steps = [
    ('scalar', StandardScaler()),
    ('poly', PolynomialFeatures(degree=2)),
    ('model', Ridge(alpha=10, fit_intercept=True))
]

ridge_pipe = Pipeline(steps)
ridge_pipe.fit(X_train, y_train)
print('\n Ridge Pipe')
print('Training Score: {}'.format(ridge_pipe.score(X_train, y_train)))
print('Test Score: {}'.format(ridge_pipe.score(X_test, y_test)))
y_pred = ridge_pipe.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
rmse = math.sqrt(mse)

print('RMSE: {}'.format(rmse))

steps = [
    ('scalar', StandardScaler()),
    ('poly', PolynomialFeatures(degree=2)),
    ('model', Lasso(alpha=0.25, fit_intercept=True))
]

lasso_pipe = Pipeline(steps)

lasso_pipe.fit(X_train, y_train)
print('\n Lasso Pipe')
print('Training score: {}'.format(lasso_pipe.score(X_train, y_train)))
print('Test score: {}'.format(lasso_pipe.score(X_test, y_test)))
y_pred = lasso_pipe.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
rmse = math.sqrt(mse)
print('RMSE: {}'.format(rmse))


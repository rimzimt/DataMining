# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 23:11:34 2019

@author: Rimzim
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 22:35:57 2019

@author: Rimzim
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,classification_report
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf


dataset = pd.read_csv('E:\\BreastCancer.csv')

#print(dataset.shape)
#print(dataset.info())

dataset = dataset.drop('Unnamed: 0',axis=1)

print(dataset.info())


# count number of obvs in each class
benign, malignant = dataset['Class'].value_counts()
print('Number of cells labeled Benign: ', benign)
print('Number of cells labeled Malignant : ', malignant)
print('')
print('% of cells labeled Benign', round(benign / len(dataset) * 100, 2), '%')
print('% of cells labeled Malignant', round(malignant / len(dataset) * 100, 2), '%')

# Split the data into training and testing sets
X = dataset
y = dataset['Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=40)

# Create a string for the formula
cols = dataset.columns.drop('Class')
formula = 'Class ~ ' + ' + '.join(cols)
print(formula, '\n')

# Run the model and report the results
model = smf.glm(formula=formula, data=X_train, family=sm.families.Binomial())
logistic_fit = model.fit()

print(logistic_fit.summary())

# predict the test data and show the first 5 predictions
predictions = logistic_fit.predict(X_test)
print(predictions[1:6])


# Convert these probabilities into nominal values 
predictions_nominal = [ "malignant" if x < 0.5 else "benign" for x in predictions]
print(predictions_nominal[1:6])


print(classification_report(y_test, predictions_nominal, digits=3))

cfm = confusion_matrix(y_test, predictions_nominal)

true_negative = cfm[0][0]
false_positive = cfm[0][1]
false_negative = cfm[1][0]
true_positive = cfm[1][1]

print('Confusion Matrix: \n', cfm, '\n')

print('True Negative:', true_negative)
print('False Positive:', false_positive)
print('False Negative:', false_negative)
print('True Positive:', true_positive)
print('Correct Predictions', 
      round((true_negative + true_positive) / len(predictions_nominal) * 100, 1), '%')



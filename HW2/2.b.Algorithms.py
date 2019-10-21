#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 16:12:00 2019

@author: rimzimthube
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier

pd.set_option('display.max_columns', 500)

df=pd.read_csv('/Users/rimzimthube/MS/Data Mining/HW2/adult.csv')
 
#print(df.head())


#df['income']=df['income'].map({' <=50K': 0, ' >50K': 1, ' <=50K.': 0, ' >50K.': 1})


#df.info()

#print(df.isnull().sum())

# %%



category_df=df.select_dtypes(include=['object'])

#print(category_df.info())

le=LabelEncoder()

category_df= category_df.apply(le.fit_transform)

df = df.drop(category_df.columns, axis=1)

df = pd.concat([df, category_df], axis=1)


# %%

X=df.drop(['income'],axis=1)
y=df['income']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)

#print(X_train.info())

# %%

lr=LogisticRegression()
lr.fit(X_train,y_train)

pred_y=lr.predict(X_test)

print('Logistic Regression Accuracy:' + format(metrics.accuracy_score(y_test,pred_y)))


#%%

dt=DecisionTreeClassifier(criterion='gini',random_state=24,max_depth=10)

dt.fit(X_train,y_train)

tree_pred_y=dt.predict(X_test)

print('\n Decision Tree Accuracy:'+ format(metrics.accuracy_score(y_test,tree_pred_y)))


print('\n Logistic Regression Precision score:'+format(metrics.precision_score(y_test,pred_y)))
print('\n Decision Tree Precision score:'+format(metrics.precision_score(y_test,tree_pred_y)))

print('\n Logistic Regression ROC AUC score:'+format(metrics.roc_auc_score(y_test,pred_y)))
print('\n Decision Tree ROC AUC score:'+format(metrics.roc_auc_score(y_test,tree_pred_y)))

print('\n Logistic Regression Recall score:'+format(metrics.recall_score(y_test,pred_y)))
print('\n Decision Tree Recall score:'+format(metrics.recall_score(y_test,tree_pred_y)))





# %%





# =============================================================================
# categorical = [' workclass', ' education', ' marital-status', ' occupation', ' moving relationship', ' race', ' sex', ' native-country']
# 
# for feature in categorical:
#     le = preprocessing.LabelEncoder()
#     X_train[feature] = le.fit_transform(X_train[feature])
#     X_test[feature] = le.fit_transform(X_test[feature])
# =============================================================================
    

#print(X_train)


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 00:02:43 2019

@author: rimzimthube
"""
from sklearn.datasets import load_breast_cancer
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score,confusion_matrix


loadedCancerData=load_breast_cancer()

#Copy attribute and target data
cancerData=np.c_[loadedCancerData.data,loadedCancerData.target]

#Create the header
header=np.append(loadedCancerData.feature_names,["target"])

#Create Dataframe of the data
cancer_df=pd.DataFrame(cancerData,columns=header)

#Separate target variable from the data
X_data=cancer_df.drop(['target'],axis=1)
Y_data=cancer_df['target']

#Create the training and test data
X_train, X_test, y_train, y_test=train_test_split(X_data,Y_data,test_size=0.33)

#SVM model
model=SVC(kernel='linear')
model.fit(X_train,y_train)

y_predict=model.predict(X_test)

#Confusion matrix
cm=np.array(confusion_matrix(y_test,y_predict,labels=[1,0]))
confusion=pd.DataFrame(cm,index=['Is cancer','Is healthy'],
                       columns=['Predicted cancer','Predicted healthy'])

print(confusion,'\n')

#List of support vectors
print('Count of support vectors: ',len(model.support_vectors_),'\n')
print('List of Support vectos: ',model.support_vectors_,'\n')

#Indices of support vectors
print('Indices of support vectors are: ',model.support_,'\n')

#Number of support vectors in each class 
print('Number of support vectors in each class: ',model.n_support_,'\n' )



#print(X.head())
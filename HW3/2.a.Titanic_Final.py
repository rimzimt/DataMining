#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 18:15:20 2019

@author: rimzimthube
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# make a list of all the posible Decks, the last element is used when no cabin code is present
cabin_list = ['A', 'B', 'C', 'D', 'E', 'F', 'T', 'G', 'Unknown']

# dictionary to map to generate the new feature vector
title_dictionary = {
    "capt":"Misc", 
    "col":"Misc", 
    "major":"Misc", 
    "dr":"Misc",
    "jonkheer":"Misc",
    "rev":"Misc",
    "countess":"Misc",
    "dona":"Misc",
    "lady":"Misc",
    "don":"Misc",
    "mr":"Mr",
    "mme":"Mrs",
    "ms":"Mrs",
    "mrs":"Mrs",
    "miss":"Miss",
    "mlle":"Miss",
    "master":"Master",
    "nan":"Mr"
}

# dictionary to map to generate the new feature vector
#marital_status_dictionary = {
#    "Mr":"Miss" "Master" "Mrs" "Royalty" "Officer"
#}

title_list = ['Mr','Miss','Mrs','Master', 'Misc']
def age_nan_replace(means, dframe, title_list):
    for title in title_list:
        temp = dframe['Title'] == title #extract indices of samples with same title
        dframe.loc[temp, 'Age'] = dframe.loc[temp, 'Age'].fillna(means[title]) 

#define a function that replaces the cabin code with the deck character
def search_substring(big_string, substring_list):
    for substring in substring_list:
        if substring in big_string:
            return substring
    return substring_list[-1]

# replace passenger's name with his/her title (Mr, Mrs, Miss, Master)
def get_title(string):
    import re
    regex = re.compile(r'Mr|Don|Major|Capt|Jonkheer|Rev|Col|Dr|Mrs|Countess|Dona|Mme|Ms|Miss|Mlle|Master', re.IGNORECASE)
    results = regex.search(string)
    if results != None:
        return(results.group().lower())
    else:
        return(str(np.nan))
        
def calculate_Family_Size(dframe):
    dframe['Is Alone']=1
    for row in dframe:
        if row['Size of family']<=1:
            dframe['Is Alone']=1
        elif row['Size of family']>1:
            dframe['Is Alone']=0
    
    return dframe

training_set = pd.read_csv('/Users/rimzimthube/MS/Data Mining/HW3/titanic_train.csv')
test_set = pd.read_csv('/Users/rimzimthube/MS/Data Mining/HW3/titanic_test.csv')

training_set['Title'] = training_set['Name'].apply(get_title)
test_set['Title'] = test_set['Name'].apply(get_title)
training_set['Title'] = training_set['Title'].map(title_dictionary)
test_set['Title'] = test_set['Title'].map(title_dictionary)


#Remove PassengerId column as it does not give any insights
training_set.drop('PassengerId',1, inplace=True)
test_set.drop('PassengerId',1, inplace=True)

#Family information 
training_set['Size of family'] = training_set['Parch'] + training_set['SibSp']
test_set['Size of family'] = test_set['Parch'] + test_set['SibSp']
#Is Alone
training_set['IsAlone'] = 1 
training_set['IsAlone'].loc[training_set['Size of family'] > 1] = 0 
test_set['IsAlone'] = 1 
test_set['IsAlone'].loc[test_set['Size of family'] > 1] = 0 

#Fare bin for fare
training_set['FareBin'] = pd.qcut(training_set['Fare'], 4)
test_set['FareBin'] = pd.qcut(test_set['Fare'], 4)


#Fill the other titles with Misc
print(training_set.Title.value_counts())

#Convert Age float values into int
means_title = training_set.groupby('Title')['Age'].mean()

age_nan_replace(means_title, training_set, title_list)
age_nan_replace(means_title, test_set, title_list)

training_set['Age']=training_set['Age'].astype(int)
test_set['Age']=test_set['Age'].astype(int)

training_set.to_csv('/Users/rimzimthube/MS/Data Mining/HW3/test.csv')






        


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 13:38:43 2019

@author: rimzimthube
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 12:06:59 2019

@author: rimzimthube
"""

# Make Predictions with k-nearest neighbors on the Iris Flowers Dataset
from csv import reader
from math import sqrt
import pandas as pd
from sklearn.preprocessing import LabelEncoder


# Load a CSV file
def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset

# Convert string column to float
def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())

# Convert string column to integer
def str_column_to_int(dataset, column):
    class_values = [row[column] for row in dataset]
    unique = set(class_values)
    lookup = dict()
    for i, value in enumerate(unique):
        lookup[value] = i
        print('[%s] => %d' % (value, i))
    for row in dataset:
        row[column] = lookup[row[column]]
    return lookup

# Find the min and max values for each column
def dataset_minmax(dataset):
    minmax = list()
    for i in range(len(dataset[0])):
        col_values = [row[i] for row in dataset]
        value_min = min(col_values)
        value_max = max(col_values)
        minmax.append([value_min, value_max])
    return minmax

# Rescale dataset columns to the range 0-1
def normalize_dataset(dataset, minmax):
    for row in dataset:
        for i in range(len(row)):
            row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])

# Calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
    distance = 0.0
    for i in range(len(row2)-1):
        distance += (row1[i] - row2[i])**2
    return sqrt(distance)

def manhattan_distance(row1, row2):
    distance = 0.0
    for i in range(len(row2)-1):
        distance += abs(row1[i] - row2[i])
    return (distance)

def chebyshev_distance(row1, row2):
    maximumDistance=0.0
    for i in range(len(row2)-1):
        value=abs(row1[i] - row2[i])
        if(value>maximumDistance):
            maximumDistance=value
            
    return (maximumDistance)

# Locate the most similar neighbors
def get_neighbors(train, test_row, num_neighbors):
    distances = list()
    for train_row in train:
        dist = euclidean_distance(test_row, train_row)
        distances.append((train_row, dist))
    distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(num_neighbors):
        neighbors.append(distances[i][0])
    return neighbors

def get_neighbors_manhattan(train, test_row, num_neighbors):
    distances = list()
    for train_row in train:
        dist = manhattan_distance(test_row, train_row)
        distances.append((train_row, dist))
    distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(num_neighbors):
        neighbors.append(distances[i][0])
    return neighbors

def get_neighbors_chebyshev(train, test_row, num_neighbors):
    distances = list()
    for train_row in train:
        dist = chebyshev_distance(test_row, train_row)
        distances.append((train_row, dist))
    distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(num_neighbors):
        neighbors.append(distances[i][0])
    return neighbors

# Make a prediction with neighbors
def predict_classification(train, test_row, num_neighbors):
    neighbors = get_neighbors(train, test_row, num_neighbors)
    output_values = [row[-1] for row in neighbors]
    prediction = max(set(output_values), key=output_values.count)
    return prediction

def predict_classification_manhattan(train, test_row, num_neighbors):
    neighbors = get_neighbors_manhattan(train, test_row, num_neighbors)
    output_values = [row[-1] for row in neighbors]
    prediction = max(set(output_values), key=output_values.count)
    return prediction

def predict_classification_chebyshev(train, test_row, num_neighbors):
    neighbors = get_neighbors_chebyshev(train, test_row, num_neighbors)
    output_values = [row[-1] for row in neighbors]
    prediction = max(set(output_values), key=output_values.count)
    return prediction

# Make a prediction with KNN on Iris Dataset
filename = '/Users/rimzimthube/MS/Data Mining/HW3/adultEncoded.csv'
    
#df=pd.read_csv('/Users/rimzimthube/MS/Data Mining/HW3/adult.csv')
#category_df=df.select_dtypes(include=['object'])
##print(category_df.info())
#le=LabelEncoder()
#category_df= category_df.apply(le.fit_transform)
#df = df.drop(category_df.columns, axis=1)
#df = pd.concat([df, category_df], axis=1)
##df=df.drop('age',axis=1)
#
#df.to_csv('/Users/rimzimthube/MS/Data Mining/HW3/adultEncoded.csv')

#filename='iris.csv'
dataset = load_csv(filename)


for i in range(len(dataset[0])-1):
    str_column_to_float(dataset, i)
# convert class column to integers
str_column_to_int(dataset, len(dataset[0])-1)


# define model parameter
num_neighbors = 5
# define a new record
#row = [5.7,2.9,4.2,1.3]

row=[22,311512,10,0,0,15,7,15,2,8,0,2,1,39]

row_test=[5.4,3.4,1.5,0.4]
# predict the label
label = predict_classification(dataset, row, num_neighbors)
print('Euclidean distance \n')
print('Data=%s, Predicted: %s' % (row, label))

label1=predict_classification_manhattan(dataset,row,num_neighbors)
print('\n Manhattan distance \n')
print('Data=%s, Predicted: %s' % (row, label1))

labelChebyshev=predict_classification_chebyshev(dataset,row,num_neighbors)
print('\n Chebyshev distance \n')
print('Data=%s, Predicted: %s' % (row, labelChebyshev))



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 15:30:35 2019

@author: rimzimthube
"""

# Naive Bayes Theorem

import csv
import random
import math
 
def readCSV(filename):
    lines = csv.reader(open(filename, "r"))
    
    dataset = list(lines)
    
    for i in range(len(dataset)):
        # Replace the class label text with numeric values
        if dataset[i][-1]=='malignant':
            dataset[i][-1]=0
        elif dataset[i][-1]=='benign':
            dataset[i][-1]=1
    
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]]

    return dataset

def splitData(dataset, splitRatio):
    trainDataSize = int(len(dataset) * splitRatio)
    trainDataSet = []
    datasetCopy = list(dataset)
    while len(trainDataSet) < trainDataSize:
        index = random.randrange(len(datasetCopy))
        trainDataSet.append(datasetCopy.pop(index))
    return [trainDataSet, datasetCopy]
 
def separateByClass(dataset):
    separated = {}
    for i in range(len(dataset)):
        vector = dataset[i]
        if (vector[-1] not in separated):
            separated[vector[-1]] = []
        separated[vector[-1]].append(vector)
    return separated
 
def mean(numbers):
    return sum(numbers)/float(len(numbers))
 
def stdev(numbers):
    avg = mean(numbers)
    variance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
    return math.sqrt(variance)

 
def classSummarize(dataset):  
    summary = {}
    for classVal, instances in dataset.items():
        calculatedValue=[(mean(value), stdev(value)) for value in zip(*instances)]
        del calculatedValue[-1]
        summary[classVal] = calculatedValue
    return summary
 
def calculateProbability(x, mean, stdev):
    exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
    return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent
 
def calculateClassProbabilities(summaries, inputVector):
    probabilities = {}
    for classVal, classSummaries in summaries.items():
        probabilities[classVal] = 1
        for i in range(len(classSummaries)):
            mean, stdev = classSummaries[i]
            x = inputVector[i]
            probabilities[classVal] *= calculateProbability(x, mean, stdev)
    return probabilities
            
def prediction(summary, testData):
    
    probabilities = {}
    for classVal, classSummary in summary.items():
        probabilities[classVal] = 1
        for i in range(len(classSummary)):
            mean, stdev = classSummary[i]
            x = testData[i]
            probabilities[classVal] *= calculateProbability(x, mean, stdev)
    
    bestLabel, bestProb = None, -1
    for classVal, probability in probabilities.items():
        if bestLabel is None or probability > bestProb:
            bestProb = probability
            bestLabel = classVal
    return bestLabel
 
def getPredictions(summary, testData):
    predictions = []
    for i in range(len(testData)):
        result = prediction(summary, testData[i])
        predictions.append(result)
    
#    print(predictions)
    return predictions
 
def getAccuracy(testData, predictions):
    correct = 0
    for i in range(len(testData)):
        if testData[i][-1] == predictions[i]:
            correct += 1
    return (correct/float(len(testData))) * 100.0
 
def main():
    # Store  Breast Cancer CSV file location
    filename = '/Users/rimzimthube/MS/Data Mining/HW2/BreastCancer.csv'
    splitRatio = 0.67
    
    #Read CSV file
    dataset = readCSV(filename)
    
    #Split the dataset into training and test dataset
    trainingData, testData= splitData(dataset, splitRatio)

    #Model creation
    separatedDataset = separateByClass(trainingData)
    summary=classSummarize(separatedDataset)
    
    # Get the predicted values from the mdel
    predictions = getPredictions(summary, testData)
    
    # Test the model based on predicted values and test data
    accuracy = getAccuracy(testData, predictions)
    print('Accuracy of Naive Bayes:'+format(accuracy))

 
main()
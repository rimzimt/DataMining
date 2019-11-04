#!/usr/bin/env python
"""mapper.py"""

import sys
import csv


f = sys.stdin.read().splitlines()
dataset = csv.reader(f)

#Calculate the average value of grade column
total=0
numberOfLines=0
for line in dataset:
    
    grades = line[19]
    
    try:
        numberOfLines+=1
        grades = float(grades)
        total=total+grades
        
    except ValueError:
        continue

average=total/numberOfLines

for line in dataset:
    tag = 'C'
    grades_9_12 = line[19]
    
    try:
        grades_9_12 = float(grades_9_12)
    except ValueError:
        #If the grade value in a row is null, replace it with the average value
        grades_9_12=average 
    if grades_9_12 < 5000.0:
        tag = 'A'
    elif (grades_9_12 > 10000.0 and grades_9_12 < 20000.0):
        tag = 'B'
    print '%s %s' % (grades_9_12, tag)

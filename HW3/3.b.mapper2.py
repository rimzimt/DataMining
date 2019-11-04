#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 23:30:35 2019

@author: rimzimthube
"""

#!/usr/bin/env python
"""mapper.py"""

import sys
import csv


f = sys.stdin.read().splitlines()
dataset = csv.reader(f)


for line in dataset:
    tag = 'C'
    grades_9_12 = line[19]
    
    try:
        grades_9_12 = float(grades_9_12)
    except ValueError:
        #If the value is null, delete the row from the dataset
        del line
        continue
    if grades_9_12 < 5000.0:
        tag = 'A'
    elif (grades_9_12 > 10000.0 and grades_9_12 < 20000.0):
        tag = 'B'
    print '%s %s' % (grades_9_12, tag)

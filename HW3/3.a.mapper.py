#!/usr/bin/env python
"""mapper.py"""

import sys
import csv

f = sys.stdin.read().splitlines()
csv_line = csv.reader(f)
for row in csv_line:
    tag = 'C'
    grades_9_12 = row[19]
    try:
        grades_9_12 = float(grades_9_12)
    except ValueError:
        continue
    if grades_9_12 < 5000.0:
        tag = 'A'
    elif (grades_9_12 > 10000.0 and grades_9_12 < 20000.0):
        tag = 'B'
    print '%s %s' % (grades_9_12, tag)

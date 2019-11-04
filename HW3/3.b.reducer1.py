#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

tag_count = {}
tag_to_category = {'A': 'Less than 5000',
        'B': 'Less than 20000, More than 10000'}

for line in sys.stdin:
    line = line.strip()
    grades_9_12, tag = line.split(' ', 1)
    try:
        grades_9_12 = float(grades_9_12)
    except ValueError:
        continue
    try:
        tag_count[tag] += 1
    except KeyError:
        tag_count[tag] = 1

for tag in tag_count.keys():
    try:
        print (tag_to_category[tag], tag_count[tag])
    except KeyError:
        continue

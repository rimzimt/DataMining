#!/usr/bin/python3
import statistics
import math

# marks and num_students are inputs for this program.
# for this assignment, both the inputs are hardcoded.
marks = [ 47, 63, 71, 39, 47, 49, 43, 37, 81, 69, 38, 13, 29, 61, 49, 53, 57, 23, 58, 17, 73, 33, 29 ]
num_students = 23

# grades is a dictionary with key as a bucket index,
# and value as a tuple of list of all the grades and 
# grade string.
# Bucket index is nothing but a integer exquivalent
# of a grade. bucket index is calculated by
# (mark - mean)/(1/3 * standard_deviation)

grades = {
            5  : ([], "A+"),
            4  : ([], "A " ),
            3  : ([], "A-"),
            2  : ([], "B+"),
            1  : ([], "B " ),
            0  : ([], "B-"),
            -1 : ([], "C+"),
            -2 : ([], "C " ),
            -3 : ([], "C-"),
            -4 : ([], "F " ),
        }

# using statistics library to calculate mean and
# standard deviation.
mean = int(round(statistics.mean(marks)))
sd = statistics.stdev(marks)
step = sd/3
print ("\nmean ", mean)
print ("Standard Deviation ", round(sd, 2))

# Calculate grade for each student in o(n) time.
print ("\n-----------------------")
print ("Grades for each student")
print ("-----------------------")
for individualMark in marks:
    
    if (individualMark > mean):
        bucket = int(math.ceil((individualMark-mean)/step))
    else:
        # special case for bucket < 0.
        bucket = int(math.floor((individualMark-mean)/step))
    
    if (bucket > 5): # anything above bucket 5 is A+
        bucket = 5
    elif (bucket < -4): # anything below bucket -4 is F
        bucket = -4
    elif (bucket == 0 and mean != individualMark):
        # only if individualMark == mean should be 
        # considered as B-, ie bucket 0. Otherwise, 
        # adjust the bucket.
        if (individualMark > mean):
            bucket = 1
        if (individualMark < mean):
            bucket = -1

    grades[bucket][0].append(individualMark)
    print (individualMark, grades[bucket][1])

# Print all the marks per grade bucket
print ("\n----------------------")
print ("Class report per grade")
print ("----------------------")
for grade in grades:
    print (grades[grade][1], end =" ")
    for pgrade in grades[grade][0]:
        print (pgrade, end =" ")
    print ()

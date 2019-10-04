#!/usr/bin/python
import statistics
import math

marks = [ 47, 63, 71, 39, 47, 49, 43, 37, 81, 69, 38, 13, 29, 61, 49, 53, 57, 23, 58, 17, 73, 33, 29 ]
num_students = 23
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

mean = int(round(statistics.mean(marks)))
sd = statistics.stdev(marks)
step = sd/3
print(step)
print ("mean ", mean)
print ("Standard Deviation ", round(sd, 2))

# Print grade for each student
for individualMark in marks:
    
    if (individualMark > mean):
        bucket = int(math.ceil((individualMark-mean)/step))
    else:
        bucket = int(math.floor((individualMark-mean)/step))
   
    
    if (bucket > 5):
        bucket = 5
    elif (bucket < -4):
        bucket = -4
    elif (bucket == 0 and mean != individualMark):
        if (individualMark > mean):
            bucket = 1
        if (individualMark < mean):
            bucket = -1

    grades[bucket][0].append(individualMark)
    print (individualMark, grades[bucket][1])

# Print all the marks per grade bucket
for grade in grades:
    print ()
    print (grades[grade][1], end =" ")
    for pgrade in grades[grade][0]:
        print (pgrade, end =" ")

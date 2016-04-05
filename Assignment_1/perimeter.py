# measures the perimeter of stuff
# By Jordan Stewart, z3291315
# input is x1 y1 x2 y2

import sys
import re
import unittest


# calculate the perimeter of each rectangle - done
# calculate the crossing other area
# subtract the overlap


# calculates the perimeter
def calculate_perimeter(x1,y1,x2,y2):
    # calculate perimeter of the rectangle thingy
    return (x2 - x1)*2 + (y2 - y1)*2

def is_overlapping(check, rectangle):
    [x1,y1,x2,y2] = check
    [x3,y3,x4,y4] = rectangle
    boolean = False
    # if
    return boolean

def between_line(x1,y1,x3,x4,y3,y4):
    if (x1 > x3 and x1 < x4) and ( y1 > y3 and y1 < y4 ):
        return True
    else:
        return False



def subtract_overlap(rectangles):
    check_me = rectangles.pop()

    for rectangle in rectangles:
        overlap = is_overlapping(check_me,rectangle)
        if overlap:
            subtract stuff proportion

    return per

# inputting text from https://www.quora.com/How-can-I-read-a-string-from-a-text-file-using-Python

# input is like file.txt
text_file = input('Which data file do you want to use? ')
# assumes there is a text file called that
f = open(text_file)
lines = f.readlines()  # return a list of lines in file

vertexes = []
list_of_rectangles = []
perimeter_Val = 0

for line in lines:
    vertexes = line.split()        # splits lines at space by default
    vertexes = [ int(x) for x in vertexes ] # change to ints
    perimeter_Val += calculate_perimeter(*vertexes)
    # check for overlap with backwards for loop
    list_of_rectangles.append(vertexes)
    perimeter_Val -= subtract_overlap(list_of_rectangles)


f.close()

print(list_of_rectangles)

#print("The perimeter is:", permeterVal)
# measures the perimeter of stuff
# By Jordan Stewart, z3291315
# input is x1 y1 x2 y2

# there is a lot of repeated code I could reduce with design patterns

import sys
import re
import unittest


# OO, here we go!
class CrossSection:
    def __init__(self, x1, y1,x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    # I should rewrite this to use the objects variables
    def max_point(self, old_x1, new_x1):
        if old_x1 < new_x1:
            old_x1 = new_x1
        return old_x1


    # I should rewrite this to use the objects variables
    def min_point(self, old_x1, new_x1):
        if old_x1 > new_x1:
            old_x1 = new_x1
        return old_x1

# calculate the perimeter of each rectangle - done
# calculate the crossing other area
# subtract the overlap


# calculates the perimeter
def calculate_perimeter(x1,y1,x2,y2):
    # calculate perimeter of the rectangle thingy
    return (x2 - x1)*2 + (y2 - y1)*2


# x1/y1 is the minium, x2/y2 is the max,
def max_points(points):
    x1 = y1 = x2 = y2 = 0
    for point in points:
        x1 = point.max_point(x1, point.x1)
        y1 = point.max_point(y1, point.y1)
        x2 = point.max_point(x2, point.x2)
        y2 = point.max_point(y2, point.y2)
    return [x1, y1, x2, y2]


def min_points(points):
    x1 = y1 = x2 = y2 = 0
    for point in points:
        x1 = point.min_point(x1, point.x1)
        y1 = point.min_point(y1, point.y1)
        x2 = point.min_point(x2, point.x2)
        y2 = point.min_point(y2, point.y2)
    return [x1, y1, x2, y2]


def initialise_map(points):
    buffer = 10
    [max_x1, max_y1, max_x2, max_y2] = max_points(points)
    [min_x1, min_y1, min_x2, min_y2] = min_points(points)
    map = [[0 for x in range(min_x1, max_x2)] for y in range(min_y1, max_y2)]
    return [map, min_x1, min_y1]


# min_x and min_y are the origin
# prints all the rectangles onto the map
def print_rectangles_on_map(points, map, min_x, min_y):
    buffer = 10
    print_points_scaled(points,min_x,min_y,buffer)
    # print rectangle onto map by making map have 1s on it
    for point in points:
        #xloc = range(point.x1,point.x2)
        #yloc = range(point.y1,point.y2)
        #xloc = range(point.x1+buffer+min_x,point.x2+buffer+min_x)
        #yloc = range(point.y1+buffer+min_y,point.y2+buffer+min_y)
        #map = [[1 for x in xloc] for y in yloc]
        #map = [[1 for x in xloc] for y in yloc]
        #print(xloc, yloc)   # not scaled
        #print("=====================")
                            # scaled
        xloc = range(point.x1-min_x,point.x2-min_x)
        yloc = range(point.y1-min_y,point.y2-min_y)
        print(xloc, yloc)   # not scaled

        for x in xloc:
            for y in yloc:
                map[y][x]=1
        # find min and max points something like the initialise map function
        #for x in range(point.x1, point.x2):
        #    for y in range(point.y1, point.y2):
        #        pass
                # map[x + point.x1 - min_x + buffer ][ y + point.y1 - min_y + buffer]=1
                # print("x is: ",point.x1 - min_x + buffer, "y is: ",point.y1 - min_y + buffer)
        #print("x: ",point.x1,"y: ",point.y1)
    #print_points(points)

    # map[[1 for x in range(point.x1, point.x2)] for y in range(point.y1, point.y2)]
    return map


def find_perimeter(map):
    pass


def print_points(points):
    for point in points:
        print("x1: ", point.x1,"y1: ", point.y1,"x2: ", point.x2,"y2: ", point.y2)


def print_points_scaled(points,x_min,y_min,buffer):
    for point in points:
        print("x: ", point.x1-x_min+buffer, point.x2-x_min+buffer,"y: ", point.y1-y_min+buffer, point.y2-y_min+buffer)


def print_map(map):
    for row in map:
        for col in row:
            sys.stdout.write(str(col))
        sys.stdout.write("\n")


# input is like file.txt
#text_file = input('Which data file do you want to use? ')
text_file="frames_1.txt" # TODO change me
f = open(text_file)
lines = f.readlines()
points = []
try:
    #print (lines)
    for line in lines:
        line = line.split()        # splits lines at space by default
        line = CrossSection(int(line[0]),int(line[1]),int(line[2]),int(line[3]))
        points.append(line)
except ValueError:
    print('Incorrect input, giving up...')
    sys.exit()

f.close()
# [print(point.x1, point.y1, point.x2, point.y2) for point in points]


# points[1 .. n].x1 x2 y1 y2
# initialise map
[map, min_x, min_y] = initialise_map(points)
# input to map
print("x length: ", len(map[0])," y length: ", len(map)) # print x and y length
#print_map(map)

map = print_rectangles_on_map(points, map, min_x, min_y)
# find lines on map
print_map(map)
# something like:
#print('\n'.join([''.join(['{:map[0]}'.format(item) for item in row])
#      for row in map]))
# http://stackoverflow.com/questions/17870612/printing-a-two-dimensional-array-in-python
# lines = find_perimeter(map)
# calculate perimeter
# perimeter = calculate_perimeter(lines)



# print(list_of_rectangles)

# print("The perimeter is:", perimeter)
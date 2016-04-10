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
    map = [[0 for x in range(min_x1-buffer, max_x2+buffer)] for y in range(min_y1-buffer, max_y2+buffer)]
    return [map, min_x1, min_y1]


# min_x-buffer and min_y-buffer are the origin
# prints all the rectangles onto the map
# print rectangle onto map by making map have 1s on it
def print_rectangles_on_map(points, map, min_x, min_y):
    buffer = 10
    print_points_scaled(points,min_x,min_y,buffer)
    for point in points:
        xloc = range(point.x1-min_x+buffer,point.x2-min_x+buffer)
        yloc = range(point.y1-min_y+buffer,point.y2-min_y+buffer)
        for x in xloc:
            for y in yloc:
                map[y][x]=1
    return map


def find_perimeter(map):
    [map, perimeterV] = get_vertical_lines(map)
    [map, perimeterH] = get_horizontal_lines(map)
    perimeter = perimeterV + perimeterH
    return [perimeter, map]


# got through two lines at a time
# change number to 2
def get_vertical_lines(map):
    x = 0
    y = 0
    perimeter = 0
    while x + 1 < len(map[0]):
        while y < len(map):
            if map[y][x] != map[y][x+1]:
                if map[y][x] == 1 or map[y][x] == 2:
                    map[y][x] = 2
                    # add perimeter
                    perimeter += 1
                elif map[y][x+1] == 1 or map[y][x+1] == 2:
                    map[y][x+1] = 2
                    # add perimeter
                    perimeter += 1

            y += 1
        y = 0
        x += 1
    return [map, perimeter]


# got through two lines at a time
# change number to 2
def get_horizontal_lines(map):
    x = 0
    y = 0
    perimeter = 0
    while y + 1 < len(map):
        while x < len(map[0]):
            if map[y][x] != map[y+1][x]:
                if map[y][x] == 1 or map[y][x] == 2:
                    # map[y][x] = 2
                    # add perimeter
                    perimeter += 1
                elif map[y+1][x] == 1 or map[y+1][x] == 2:
                    # map[y+1][x] = 2
                    # add perimeter
                    perimeter += 1
            x += 1
        x = 0
        y += 1
    return [map, perimeter]


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

# initialise map
[map, min_x, min_y] = initialise_map(points)
# input to map
map = print_rectangles_on_map(points, map, min_x, min_y)
# find lines on map
[perimeter, map] = find_perimeter(map)
print(perimeter)
print_map(map)
# calculate perimeter
# perimeter = calculate_perimeter(lines)

# print_map(map)

# print("The perimeter is:", perimeter)
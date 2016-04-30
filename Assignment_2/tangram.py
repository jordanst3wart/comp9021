# by Jordan Stewart
# Worse is better

import re
import math

# 1. is input valid
# 2. two files are identical
# 3. are a solution to a tangram puzzle


class Tangram():
    pass


# available_coloured_pieces(file)


# open for xml types might not be defined
# opens the file, I might not need to write this
# def open(’pieces_AA.xml’)


# return true if valid pieces
def are_valid(coloured_pieces):
    for piece in coloured_pieces:
        if not(piece.check_angle()) or not(piece.check_sides()):
            return False
    return True

# return pieces ( a list of pieces), a piece is a list of points
def available_coloured_pieces(file):
    # I would like to map
    return list(map(parse_xml,file))


# input could be file but the file should be iterateable
# returns piece, a list of points
def parse_xml(line):
    if "svg" in line:
        pass    # might return something weird
    piece = []
    line=re.split('\"',line)
    line=line[1].split()
    for string in line:
        if string:
            pass
        else:
            piece.append(Point(string,string.next)) # might not remove from que
    return piece


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    # get true bearing angle from two points
    def get_angle(self,point):
        # get gradient
        # TODO do maths for this part
        angle = math.atan2((point.y - self.y),(point.x - self.x))
        angle = 90 - angle
        return angle


# a group of points
class Piece():
    def __init__(self,point_list):
        self.point_list = point_list

    # convex and clockwise angles
    def check_angle(self):
        angles = []
        size = len(self.point_list)
        i=0
        while i <= size:
            if i == size: # last
                angles.append(self.point_list[i].get_angle(self.point_list[0]))
            else:
                angles.append(self.point_list[i].get_angle(self.point_list[i+1]))

        # get a list of true bearings
        # check if ascending or descending
        # substraction previous angle
        # all should be below 180
        return True

    def check_sides(self):
        if len(self.point_list)<3:
            return False
        else:
            return True








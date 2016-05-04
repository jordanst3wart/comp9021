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
def are_valid(pieces):
    for piece in pieces:
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
    def get_bearing(self,point):
        # get gradient
        angle = math.atan2((point.y - self.y),(point.x - self.x))
        # return between pi and -pi from the horizontal
        if angle < 0:
            angle = self.change_angle_range(angle)
        angle = 90 - angle # make from the vertical axis
        return angle

    # static method
    def change_angle_range(angle):
            return 2*math.fab(angle)


# a group of points
class Piece:
    def __init__(self,point_list):
        self.point_list = point_list

    # convex and clockwise angles
    def check_angle(self):
        angles = []
        size = len(self.point_list)
        i=0
        while i <= size:
            if i == size: # last point
                angles.append(self.point_list[i].get_bearing(self.point_list[0]))
            else:
                angles.append(self.point_list[i].get_bearing(self.point_list[i+1]))
            diff = [right-left for left, right in zip(angles, angles[1:]+angles[:1])] # got from question I asked on stack
            if diff[-2]>0: # could look at a ternary operator here
                diff[-1] = diff[-1] + 360
            else:
                diff[-1] = diff[-1] - 360
            # TODO need to input angles from start point into clockwise_angle_check
            # diff is only good for adjacent angle check
        return self.clockwise_angle_check(diff) and self.difference_in_adjacent_angle_check(diff)

    # static method
    # checks if angles are ascending or descending
    def clockwise_angle_check(diff):
        # static method - I did this so I didn't have to add 'self' to the args
        def times_negative_one(val):
            return val * -1

        def if_ascending(diff):
            # TODO do logic stuff checking if the angle is ascending
            return True

        # make ascending if descending
        # should remove else statement
        if diff[0]<0:
            return if_ascending(list(map(times_negative_one,diff)))
        else:
            return if_ascending(diff)






    # static method
    # checks if angles are not different by 180 degrees (convex)
    def difference_in_adjacent_angle_check(angles):
        return True


    def check_sides(self):
        if len(self.point_list)<3:
            return False
        else:
            return True








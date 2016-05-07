# by Jordan Stewart
# Worse is better

import re
import math

import unittest

# 1. is input valid - done needs testing
# 2. two files are identical - done needs testing
# 3. are a solution to a tangram puzzle


class Tangram():
    pass


# available_coloured_pieces(file)


# open for xml types might not be defined
# opens the file, I might not need to write this
# def open(’pieces_AA.xml’)

# maybe? if equals works for list of the class
def are_identical_sets_of_coloured_pieces(pieces,other_pieces):
    return pieces == other_pieces
    #bool = True
    #for piece in pieces:
    #    for other_piece in other_pieces:
    #        if piece != other_pieces:
    #            bool = False
    #return bool

#  tiling puzzle
# http://stackoverflow.com/questions/31097669/a-algorithm-while-solving-sliding-tile-puzzle-executes-for-a-very-long-time
def is_solution(tangram, shape):
    # shape is one piece in a pieces array
    # if area is not equal then false, quick win?
    # need piece calculate area by breaking into triangles
    # implement that for a list of pieces with map
    pass

    #options??
    # BFS

    # a star search





# return true if valid pieces
def are_valid(pieces):
    bool = True
    for piece in pieces:
        print(piece)
        if not(piece.check_angles() and piece.check_sides()):
            bool = False
    return bool


# return pieces ( a list of pieces), a piece is a list of points
def available_coloured_pieces(file):
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def create_point_list(vals):
        point_list = []
        for i in range(0, len(vals)-1,2): #vals: #range(0, len(l)):
            point_list.append(Point(vals[i],vals[i+1]))
        return point_list
    pieces = []
    piece = []
    temp = []
    piece_list = []
    for line in file:
        line = parse_xml(line)
        if line is not None:
            for val in line:
                if is_number(val):
                    piece.append(val)
            pieces.append(piece)
            piece = []
    for piece in pieces:
        temp.append(create_point_list(piece))
    for piece in temp:
        piece_list.append(Piece(piece))
    return piece_list

# input could be file but the file should be iterateable
# returns piece, a list of points
def parse_xml(line):
    #print(line)
    if "svg" in line or len(line)<2:
        return None   # might return something weird
    #print(line)
    vals = []
    line=re.split('\"',line)
    line=line[1].split()
    for string in line:
        if string:
            vals.append(string)
            #piece.append(Point(string,string.next)) # might not remove from que
            #print("full string:  ", string)
    return vals


class Point:
    def __init__(self,x,y):
        self.x = int(x)
        self.y = int(y)

    def __repr__(self):
        return "Point({},{})".format(self.x,self.y)

    def __str__(self):
        return "Point({},{})".format(self.x,self.y)

    # get true bearing angle from two points
    def get_bearing(self,point):
        def to_degree(angle):
            return angle*180/math.pi
            # static method, converts -pi to 2pi
        def change_angle_range(angle):
            return 2*abs(angle)
        # get gradient
        angle = math.atan2((point.y - self.y),(point.x - self.x))
        # return between pi and -pi from the horizontal
        if angle < 0:
            angle = change_angle_range(angle)
        angle = 90 - to_degree(angle) # make from the vertical axis
        return angle

    # overriding equals for Point class
    def __eq__(self, other):
        #bool = False
        #if self.x == other.x and self.y == other.y:
        #    bool = True
        #return bool
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    # overriding not equal for Point class
    def __ne__(self, other):
        #bool = False
        #if not(self.x == other.x and self.y == other.y):
        #    bool = True
        #return bool
        if type(other) is type(self):
            return not(self.__dict__ == other.__dict__)
        return True


# a group of points
class Piece:
    def __init__(self,point_list):
        self.point_list = point_list

    # should work?
    def __eq__(self, other):
        #return self.point_list == other.point_list
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    def __ne__(self, other):
        #return self.point_list != other.point_list
        if type(other) is type(self):
            return not(self.__dict__ == other.__dict__)
        return True

    def __repr__(self):
        return "Piece({})".format(self.point_list)

    def __str__(self):
        return "Piece({})".format(self.point_list)

    # convex and clockwise angles
    def check_angles(self):
        angles = []
        size = len(self.point_list)
        i=0
        diff = []
        while i <= size:
            if i == size: # last point
                angles.append(self.point_list[i].get_bearing(self.point_list[0]))
            else:
                angles.append(self.point_list[i].get_bearing(self.point_list[i+1]))
            diff = [right-left for left, right in zip(angles, angles[1:]+angles[:1])] # got from question I asked on stack
            if diff[0]>0: # if the list if positive
                diff[-1] += + 360
            else:
                diff[-1] += - 360

            if len(diff)<3:
                print(diff)
            i += 1
            # TODO need to input angles from start point into clockwise_angle_check
            # diff is only good for adjacent angle check
        return self.clockwise_angle_check(diff) and self.difference_in_adjacent_angle_check(diff)

    # static method
    # checks if angles are ascending or descending to make sure they are defined clockwise or anti-clockwise
    def clockwise_angle_check(diff):
        # static method - I did this so I didn't have to add 'self' to the args
        def times_negative_one(val):
            return val * -1

        def if_ascending(diff):
            return sorted(diff) == diff

        bool = False
        if diff[0] < 0:
            bool = if_ascending(list(map(times_negative_one,diff)))
        else:
            bool = if_ascending(diff)

        return bool

    def check_sides(self):
        if len(self.point_list)<3:
            return False
        else:
            return True

    # check if all angles are below 180
    def difference_in_adjacent_angle_check(diff):
        bool = True
        for angle in diff:
            if angle > 180:
                bool = False
        return bool



class Q1(unittest.TestCase):

    def test_are_valid(self):
        file = open('pieces_A.xml')
        coloured_pieces = available_coloured_pieces(file)
        self.assertTrue(are_valid(coloured_pieces))
        #file = open('pieces_AA.xml')
        #coloured_pieces = available_coloured_pieces(file)
        #self.assertTrue(are_valid(coloured_pieces))
        #file = open('incorrect_pieces_2.xml')
        coloured_pieces = available_coloured_pieces(file)
        #self.assertFalse(are_valid(coloured_pieces))
        #file = open('incorrect_pieces_3.xml')
        coloured_pieces = available_coloured_pieces(file)
        #self.assertFalse(are_valid(coloured_pieces))
        #file = open('incorrect_pieces_4.xml')
        coloured_pieces = available_coloured_pieces(file)
        #self.assertFalse(are_valid(coloured_pieces))



def main():
    file = open('pieces_A.xml')
    coloured_pieces = available_coloured_pieces(file)
    are_valid(coloured_pieces)


# if is run directly
if __name__ == '__main__':
    #unittest.main()
    main()




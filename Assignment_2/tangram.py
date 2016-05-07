# by Jordan Stewart

import re
import math
import unittest

# Questions
# 1. is input valid - done needs testing
# 2. two files are identical - done needs testing
# 3. are a solution to a tangram puzzle


class Tangram():
    pass

# open for xml types might not be defined
# opens the file, I might not need to write this
# def open(’pieces_AA.xml’)

# maybe? if equals works for list of the class
def are_identical_sets_of_coloured_pieces(pieces,other_pieces):
    bool = False

    for piece in pieces:
        for other in other_pieces:
            if piece == other:
                bool = True
        if bool == False:
            return False
        bool = False
    return True

    #return pieces == other_pieces
    # TODO compare the diff in angles and a scale ie. area?
    # TODO make an area cal
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
# TODO up to this
def are_valid(pieces):
    bool = True
    for piece in pieces:
        #print("angle check: ", piece.check_angles(),"  side check: ", piece.check_sides())
        if piece.check_angles() and piece.check_sides():
            #print("Not Legit : ",piece)
            bool = True
        else:
            bool = False
            #print("Legit : ", piece)
    return bool

# return pieces ( a list of pieces), a piece is a list of points
# I would like to make this a class or something, it feels to big to be a function
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

    # return a list of values
    def parse_xml(line):
        vals = []
        if "svg" in line or len(line)<2:
            return None
        line=re.split('\"',line)
        line=line[1].split()
        for string in line:
            if string:
                vals.append(string)
        return vals

    def get_values(file):
        # I should break this down into functions
        pieces = []
        piece = []
        for line in file:
            line = parse_xml(line)
            if line is not None:
                for val in line:
                    if is_number(val):
                        piece.append(val)
                pieces.append(piece)
                piece = []
        return pieces

    def create_pieces(values):
        temp = []
        for value in values:
            temp.append(Piece(create_point_list(value)))
        return temp

    values = get_values(file)
    pieces = create_pieces(values)
    return pieces




class Point:
    def __init__(self,x,y):
        self.x = int(x)
        self.y = int(y)

    def __repr__(self):
        return "Point({},{})".format(self.x,self.y)

    def __str__(self):
        return "Point({},{})".format(self.x,self.y)

    # get angle from two points from the x horizontal
    def get_angle(self,point):
        # get gradient
        angle = math.atan2((point.y - self.y),(point.x - self.x))
        # return between pi and -pi from the horizontal
        if angle < 0:
            angle = self.change_angle_range(angle)
        # retrun between 0 and 2 pi
        return self.to_degree(angle) # change to degrees

    @staticmethod
    def change_angle_range(angle):
        return 2*math.pi + angle

    # static method, converts -pi to 2pi
    @staticmethod
    def to_degree(angle):
        return angle*180/math.pi


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
        self.remap = True
        self.angles = self.create_angles()
        self.diff = self.create_diff()
        # self.area

    # should work?
    def __eq__(self, other):
        #return self.point_list == other.point_list
        if type(other) is type(self):
            print("This: ",sorted(self.diff), "That:",sorted(other.diff))
            bool = sorted(self.diff) == sorted(other.diff)
            if bool == True:
                print("returned True!!!!")
            return bool
        return False
        # TODO this make it compare diff angle and area
        # will need to sort the angles

    def __ne__(self, other):
        return not(self.__eq__(other))
        #return self.point_list != other.point_list
        #if type(other) is type(self):
        #    return not(self.__dict__ == other.__dict__)
        #return True
        # TODO this make it compare diff angle and area

    def __repr__(self):
        return "Piece({})".format(self.point_list)

    def __str__(self):
        return "Piece({})".format(self.point_list)

    def create_angles(self):
        angles = []
        size = len(self.point_list)-1
        i=0
        diff = []
        while i <= size:
            if i == size: # last point
                angles.append(self.point_list[i].get_angle(self.point_list[0]))
            else:
                angles.append(self.point_list[i].get_angle(self.point_list[i+1]))
            i += 1
        return angles

    def create_diff(self):
        diff = [self.polar_diff(right,left) for left, right in zip(self.angles, self.angles[1:]+self.angles[:1])] # got from question I asked on stack
        if all(angle < 0 for angle in diff):
            diff = list(map(self.times_negative_one,diff))
        return diff


    # convex and clockwise angles
    # TODO up to here debugging this
    def check_angles(self):
        #print(self,"  angles :", angles," diff: ",diff)
        #print(self, diff,"   clockwise check: ",self.clockwise_angle_check(diff), "adjacent angle check: ", self.difference_in_adjacent_angle_check(angles,diff))
        #print(self, diff,"   clockwise check: ",self.clockwise_angle_check(diff))
        return self.clockwise_angle_check(self.diff) and self.difference_in_adjacent_angle_check(self.angles,self.diff)

    def polar_diff(self,right,left):
        val = right-left
        temp = right-left
        if abs(val) > 180 and self.remap:
            if left<180:
                val = right - left - 360
            else:
                val = right - left + 360
            self.remap = False
            #val = val + 1000
        #print("initial diff:", temp, "final diff: ", val)
        return val

    # checks if angles are ascending or descending to make sure they are defined clockwise or anti-clockwise
    def clockwise_angle_check(self,diff):
        # static method - I did this so I didn't have to add 'self' to the args
        bool = False
        if diff[0] < 0:
            diff = list(map(self.times_negative_one,diff))
            #print("diff reverse: ",list(map(self.times_negative_one,diff)))
            bool = all(angle > 0 for angle in diff)
        else:
            bool = all(angle > 0 for angle in diff)
        return bool

    @staticmethod
    def times_negative_one(val):
        return val * -1

    def check_sides(self):
        if len(self.point_list)<3:
            return False
        else:
            return True


    # check if all angles are below 180
    @staticmethod
    def difference_in_adjacent_angle_check(angles,diff):
        bool = True
        for angle in diff:
            if angle > 180:
                bool = False
        return bool


# done
class Q1(unittest.TestCase):

    def test_are_valid(self):
        file = open('pieces_A.xml')
        coloured_pieces = available_coloured_pieces(file)
        self.assertTrue(are_valid(coloured_pieces))
        file.close()
        file = open('pieces_AA.xml')
        coloured_pieces = available_coloured_pieces(file)
        self.assertTrue(are_valid(coloured_pieces))
        file.close()
        file = open('incorrect_pieces_1.xml')
        coloured_pieces = available_coloured_pieces(file)
        self.assertFalse(are_valid(coloured_pieces))
        file.close()
        file = open('incorrect_pieces_2.xml')
        coloured_pieces = available_coloured_pieces(file)
        self.assertFalse(are_valid(coloured_pieces))
        file.close()
        file = open('incorrect_pieces_3.xml')
        coloured_pieces = available_coloured_pieces(file)
        self.assertFalse(are_valid(coloured_pieces)) # doesn't work :(
        file.close()
        file = open('incorrect_pieces_4.xml')
        coloured_pieces = available_coloured_pieces(file)
        self.assertFalse(are_valid(coloured_pieces)) # doesn't work :(
        file.close()

class Q2(unittest.TestCase):

        def test_are_identical_sets_of_coloured_pieces(self):
            file = open('pieces_A.xml')
            coloured_pieces_1 = available_coloured_pieces(file)
            file.close()
            file = open('pieces_AA.xml')
            coloured_pieces_2 = available_coloured_pieces(file)
            file.close()
            self.assertTrue(are_identical_sets_of_coloured_pieces(coloured_pieces_1,coloured_pieces_2))

            file = open('shape_A_1.xml')
            coloured_pieces_2 = available_coloured_pieces(file)
            file.close()
            self.assertFalse(are_identical_sets_of_coloured_pieces(coloured_pieces_1,coloured_pieces_2))




def mainQ1():
    file = open('incorrect_pieces_3.xml')
    coloured_pieces = available_coloured_pieces(file)
    are_valid(coloured_pieces)

def mainQ2():
    file = open('pieces_A.xml')
    coloured_pieces_1 = available_coloured_pieces(file)
    file.close()
    file = open('pieces_AA.xml')
    coloured_pieces_2 = available_coloured_pieces(file)
    file.close()
    print(coloured_pieces_1[0].diff)
    print(coloured_pieces_2[0].diff)
    print(are_identical_sets_of_coloured_pieces(coloured_pieces_1,coloured_pieces_2))


# if is run directly
if __name__ == '__main__':
    unittest.main()
    #mainQ1()
    #mainQ2()




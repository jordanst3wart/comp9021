# Defines two classes, Point() and Disk().
# The latter has an "area" attribute and three methods:
# - change_radius(r)
# - intersects(disk), that returns True or False depending on whether
#   the disk provided as argument intersects the disk object.
# - absorb(disk), that returns a new disk object that represents the smallest
#   disk that contains both the disk provided as argument and the disk object.
#
# Written by Jordan Stewart and Eric Martin for COMP9021


# from math import pi, hypot
import math
# what is hypot??


class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({:.2f}, {:.2f})'.format(self.x, self.y)

    def get_distance_between(self, Point):
        distance = math.sqrt( (self.x - Point.x)**2 + (self.y - Point.y)**2)
        return distance


# possibly a sub class of point
# takes the import of center and point
class Disk(Point):
    def __init__(self, centre, area):
        Point.__init__(self, *centre)
        self.radius = math.sqrt(area/math.pi)

    # print shit the Disk way
    def __repr__(self):
        return 'Disk(Point({:.2f}, {:.2f}), {:.2f})'.format(self.x, self.y,self.area)

    def change_radius(self, radius):
        self.radius = radius

    def intersects(self,disk):
        bool = False
        # get disks centers
        # calculate the distance between the centers
        # use super classes method, I don't know if inherits the method
        distance1 = self.get_distance_between(self, disk)
        # calculate the radiuses
        # add the radiuses
        # I made the radius a class property instead of area coz area is found with radius mostly,
        # and radius is more useful as a metric
        distance2 = self.radius + disk.radius
        # if true return false
        # else return true
        # if the radiuses are larger than the distances between centers
        if distance1 <= distance2:
            bool = True
        return bool

    # method with no input, needs to use no brackets
    def area(self):
        return math.pi * (self.radius ** 2)

    # I'm guessing make disks make the same centre
    def absorb(self):
        # find the area between the two centres as the new centre point
        # find the distance between the two centre points
        # add the two radi to the distance
        # halve that and make it the new radius
        # eat ice-cream
        pass

            
        



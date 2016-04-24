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


    def x_distance(self,point):
        return self.x - point.x

    def y_distance(self,point):
        return self.y - point.y

    def get_distance_between(self, point):
        distance = math.sqrt(self.x_distance(point)**2 + self.y_distance(point)**2)
        return distance

    def get_half_way(self, point):
        x_distance = self.x_distance(point)/2
        y_distance = self.y_distance(point)/2
        # add distance to point but in the right direction
        # get the min point
        _x = min(point.x,self.x)+x_distance
        _y = min(point.y,self.y)+y_distance
        return Point(_x,_y)

    # breaks encapsulation but...
    def give_string(self):
        #string_format = 'Point({:.2f}, {:.2f})'.format(self.x, self.y)
        #string = eval(string_format)
        return [self.x,self.y]



# possibly a sub class of point
# takes the import of center and point
class Disk(Point):
    def __init__(self, centre = Point(0,0), radius=0.0):
        Point.__init__(self, centre.x,centre.y)
        self.radius = radius
        self.area = math.pi * radius ** 2  # redundant but lecturer asked for it
        # it should be a function but he wants disk.area not disk.area()

    def __repr__(self):
        return 'Disk(' + super().__repr__() + ', {:.2f})'.format(self.area)


    def change_radius(self, radius):
        self.radius = radius
        self.area =  math.pi * radius ** 2
        # gay but radius should be stored not area, you find area from radius not vice versa

    def intersects(self, disk):
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

    #def area(self):
    #    return self.radius ** 2 * math.pi


    # I'm guessing make disks make the same centre
    def absorb(self, disk):
        # find the distance between the two centre points
        distance = self.get_distance_between(self, disk)
        # add the two radi to the distance
        distance += self.radius + disk.radius
        # halve that
        new_area = math.pi * (distance/2 ** 2) # had to repeat :(
        # eat ice-cream
        centre = self.get_half_way(self, disk)
        return Disk(centre, new_area)




test = False



# My tests
centre = Point(0,0)
point_1 = Disk(centre,2)
point_1
centre

# There tests
if test == True:
    #>>> from quiz_6 import *
    disk_1 = Disk()
    disk_1
    #Disk(Point(0.00, 0.00), 0.00)
    disk_1.area
    #0.0
    disk_2 = Disk(Point(3, 0), 4)
    #Traceback (most recent call last):
    #  File "<stdin>", line 1, in <module>
    #TypeError: __init__() takes 1 positional argument but 3 were given
    disk_2 = Disk(centre = Point(3, 0), radius = 4)
    disk_2.area
    #50.26548245743669
    disk_1.intersects(disk_2)
    #True
    disk_2.intersects(disk_1)
    #True
    disk_3 = disk_1.absorb(disk_2)
    disk_3
    #Disk(Point(3.00, 0.00), 4.00)
    disk_1.change_radius(2)
    disk_1.area
    #12.566370614359172
    disk_3 = disk_1.absorb(disk_2)
    disk_1
    #Disk(Point(0.00, 0.00), 2.00)
    disk_2
    #Disk(Point(3.00, 0.00), 4.00)
    disk_3
    #Disk(Point(2.50, 0.00), 4.50)
    disk_4 = Disk(centre = Point(-4, 0), radius = 2)
    disk_4.intersects(disk_1)
    #True
    disk_5 = disk_4.absorb(disk_1)
    disk_5
    #Disk(Point(-2.00, 0.00), 4.00)
    disk_5.change_radius(5)
    disk_5
    #Disk(Point(-2.00, 0.00), 5.00)
    disk_6 = Disk(centre = Point(1, 2), radius = 6)
    disk_7 = disk_5.absorb(disk_6)
    disk_7
    #Disk(Point(-0.08, 1.28), 7.30)
    disk_7.area
    #167.54280759052247
    disk_8 = Disk()
    disk_8
    #Disk(Point(0.00, 0.00), 0.00)
    disk_8.change_radius(7)
    disk_8.absorb(disk_7)
    #Disk(Point(-0.05, 0.79), 7.79)
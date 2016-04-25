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
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({:.2f}, {:.2f})'.format(self.x, self.y)

    def x_distance(self,point):
        return point.x - self.x

    def y_distance(self,point):
        return point.y - self.y

    def get_distance_between(self, point):
        distance = math.sqrt(self.x_distance(point)**2 + self.y_distance(point)**2)
        return distance

    def get_half_way(self, point):
        x_distance = self.x_distance(point)/2
        y_distance = self.y_distance(point)/2
        # add distance to point but in the right direction
        # get the min point
        _x = min(point.x,self.x)+math.fabs(x_distance)
        _y = min(point.y,self.y)+math.fabs(y_distance)
        return Point(_x,_y)


# possibly a sub class of point
# takes the import of center and point
# positional arguements are all the arguements in the different positions
#
class Disk(Point):
    def __init__(self, **keywords): # , centre=Point(0,0), radius=0.0
        #super(Disk, self).__init__()    # default Point(0,0) get done in Point class
        if "centre" in keywords:
            super(Disk, self).__init__(x=keywords["centre"].x,y=keywords["centre"].y)   # centre
        else:
            super(Disk, self).__init__()  # default

        if "radius" in keywords:
            self.radius = keywords["radius"]  # radius
        else:
            self.radius = 0.0  # radius
        self.area = math.pi * self.radius ** 2  # redundant but lecturer asked for it
        # it should be a function but he wants disk.area not disk.area()

    def __repr__(self):
        return 'Disk(' + super().__repr__() + ', {:.2f})'.format(self.radius)

    def change_radius(self, radius):
        self.radius = radius
        self.area =  math.pi * radius ** 2
        # gay but radius should be stored not area, you find area from radius not vice versa

    def intersects(self, disk):
        bool = False
        # get disks centers
        # calculate the distance between the centers
        # use super classes method, I don't know if inherits the method
        #distance1 = self.get_distance_between(self, disk)
        #def baz(self, arg):
        #return super(Foo, self).baz(arg)
        distance1 = super(Disk,self).get_distance_between(disk)     # use parent method
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

    # overriding
    # returns modified half way point between two disks
    def get_half_way(self,disk):
        x_distance = super(Disk,self).x_distance(disk)
        y_distance = super(Disk,self).y_distance(disk)
        # add distance to point but in the right direction
        # get the min point
        # self before disk
        # make sure to know which points are which
        if x_distance > 0:  # self is x1
            point_1 = Point(self.x,self.y)
            point_2 = Point(disk.x,disk.y)
            rad_1 = self.radius
            rad_2 = disk.radius
        else: # disk is x1
            point_1 = Point(disk.x,disk.y)
            point_2 = Point(self.x,self.y)
            rad_1 = disk.radius
            rad_2 = self.radius
        #print("Starting x distance: ", x_distance,"y distance: ",y_distance)
        #print("Starting points: ", point_1,"  2: ",point_2)

        # in case of big circles
        if math.sqrt(x_distance**2 + y_distance**2) + rad_1 < rad_2:
            rad_1 += rad_2 - math.sqrt(x_distance**2 + y_distance**2)
        elif rad_1 > math.sqrt(x_distance**2 + y_distance**2) + rad_2:
            rad_2 += rad_1 - math.sqrt(x_distance**2 + y_distance**2)

        # avoid divide by 0
        if x_distance == 0:
            if y_distance > 0:
                rads = math.pi/2 # up
            else:
                rads = - math.pi/2  # down
        else:
            grad = y_distance/x_distance
            rads=math.atan(grad) # in radians
        # on radius points
        x_1 = - math.cos(rads) * rad_1 + point_1.x
        x_2 = math.cos(rads) * rad_2 + point_2.x
        y_1 = - math.sin(rads) * rad_1 + point_1.y
        y_2 = math.sin(rads) * rad_2 + point_2.y
        # re-use points
        point_1 = Point(x_1,y_1)
        point_2 = Point(x_2,y_2)

        x_distance = point_1.x_distance(point_2)
        y_distance = point_1.y_distance(point_2)
        #print("Final x distance: ", x_distance,"y distance: ",y_distance)
        #print("Finishing points: ", point_1,"  2: ",point_2)

        _x = min(point_1.x,point_2.x)+math.fabs(x_distance)/2
        _y = min(point_1.y,point_2.y)+math.fabs(y_distance)/2
        return Point(_x,_y)



    # TODO fix this function
    # creates a bigger disk from the smaller two
    def absorb(self, disk):
        # find the distance between the two centre points
        distance = super(Disk,self).get_distance_between(disk) + self.radius + disk.radius # I should make this a function
        # add the two radi to the distance
        #distance += self.radius + disk.radius
        # halve that
        #print("distance: ", distance) # correct??s
        radius_local = distance/2 # should be right
        if radius_local < max(self.radius,disk.radius):
            radius_local = max(self.radius,disk.radius)
        # eat ice-cream
        centre_local = self.get_half_way(disk)
        return Disk(centre=centre_local, radius=radius_local)


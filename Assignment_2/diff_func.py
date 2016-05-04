    # def difference(angle):
    #     return angle.next() - angle
    #
    # angles = [90,180,270]
    # diff = list(map(difference,angles))
    # print(diff)
    #
    # angles = [90,180,270]
    # diff = []
    # for angle in angles:
    #     diff.append(angles.next()-angle)
    #
    # print(diff)
    #
    #
    # print 90,90,-180
# angles = [90,180,270]
# i = 0
# diff = []
# angles.append(angles[0])
# while i <len(angles)-1:
#      diff.append(angles[i+1]-angles[i])
#      i += 1
#
# print(diff)
import math
#angles = [-90,-180,-270]
# 90 + 360
#diff = [right-left for left, right in zip(angles, angles[1:]+angles[:1])]
#diff[-1]=diff[-1]-360
#

#print(diff)

class SomeClass():
    def __init__(self):
        self.val=1


    def do_some_check(self):
        return self.some_check(self.val)


    def some_check(self,val):
        # another static method - I did this so I didn't have to add 'self' to the args
        def times_negative_one(val):
            return val * -1
        # another static method

        def if_positive(val):
            if val>0:
                return True
            else:
                return False

        return if_positive(times_negative_one(val))

someclass = SomeClass()
print(someclass.val)
print(someclass.do_some_check())

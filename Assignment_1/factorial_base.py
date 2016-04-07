# does factorial base stuff
# By Jordan Stewart, z3291315


import sys
import unittest
import math
#import functools


def base_factorial(term, value):
    if term <= 0:
        return [term, value]
    num = count_up_factorials(term)
    times = count_up_multi(term,num)

    value += times * 10 ** (num-1) # stored as decimal
    term = term - times * math.factorial(num) # needs to involve times

    #print('times: ', times, ' power: ', num,'value: ', value, 'term: ', term)
    [term, value] = base_factorial(term, value)
    return [term,value]


# factors finders from stack
#def factors(n):
#    return set(functools.reduce(list.__add__,
#                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def count_up_multi(term,num):
    # start at 2 to stop 1 - 1
    times = 2
    while term >= times * math.factorial(num):
        times += 1

    return times-1


# find the highest factorial base
def count_up_factorials(term):
    # start at 2 to stop 1 - 1
    top = 2
    while term >= math.factorial(top):
        top += 1

    return top - 1


try:
    term = int(input('Input a nonnegative integer : '))
    if term < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up...')
    sys.exit()

value = 0
(blah, value) = base_factorial(term,value)
# for zero factorial case :)
if term == 0:
    value = 0

print('Decimal ',term,' reads as ',value,' in factorial base.')


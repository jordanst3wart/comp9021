# Generates a list of 20 random integers between 0 and 99,
# prints out the list, computes the maximum element of the list,
# and prints it out.
#
# Written by Eric Martin for COMP9021

from random import randint


# Create a list L of 20 random integers between 0 and 99.
L = [randint(0, 99) for _ in range(20)]
# At this stage,
# - L[0] denotes the first randomnly generated number
# - L[1] denotes the second randomnly generated number
# ...
# - L[19] denotes the twentieth randomnly generated number
print('The list is:' , L)
max_element = 0
# We let i take the values 0, 1, 2, ... 19
for i in range(20):
    # If the (i+1)st element in the list, L[i], is greater than
    # the largest number seen before, then L[i] becomes the largest
    # element seen so far, recorded as max_element.
    if L[i] > max_element:
        max_element = L[i]
print('  The maximum number in this list is:', max_element)
# Of course there is an easier way;
# as so often, python just makes it too easy!
print('Confirming with builtin operation:', max(L))

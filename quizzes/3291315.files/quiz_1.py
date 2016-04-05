# Generates a list L_indexes of 12 random numbers between 0 and 3 included,
# generates a list L_values of 15 distinct random numbers between 0 and 99 included,
# and iteratively builds a list resulting_list as follows:
# - if i_1, ..., i_k is the longest initial segment of L_indexes consisting of nothing but
#   distinct numbers, then add to resulting_list the elements of L_values of index i_1, ..., i_k;
# - remove from L_indexes and L_values the numbers that have been used during the previous step.
#
# Written by Jordan Stewart and Eric Martin for COMP9021
# z3291315

import sys
from random import seed, randint, sample


nb_of_indexes = 12
max_index = 3
upper_bound = 100

try:
    seed(input('Enter an integer: '))
except TypeError:
    print('Incorrect input, giving up.')
    sys.exit()

L_indexes = [randint(0, max_index) for _ in range(nb_of_indexes)]
L_values = sample(range(upper_bound), nb_of_indexes + max_index)
print('The generated lists of indexes and values are, respectively:')
print('  ', L_indexes)
print('  ', L_values)
#print('==============================')
resulting_list = []
count = 0
while count < len(L_indexes):
    resulting_list.append(L_values[L_indexes[count]])
    # print("resulting_list:", resulting_list)  # debugging

    # print('new resulting_list:', resulting_list,'deleting: %d' % L_values[L_indexes[count]], 'Which is index %d' % L_indexes[count])
    del L_values[L_indexes[count]]
    del L_indexes[count]
    # print('Remaining list:', L_values)
    # count += 1

# REPLACE THIS COMMENT WITH YOUR CODE (aim for around 11 lines of code)

print('The resulting list of values is:')
print('  ', resulting_list)

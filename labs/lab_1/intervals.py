# Prompts the user for a strictly positive integer N,
# generates a list of N random integers between 0 and 19, prints out the list,
# computes the number of elements less 5, 10 and 15, and prints them out.
#
# Written by Eric Martin for COMP9021

from random import randint
from sys import exit


nb_of_elements = input('How many elements do you want to generate? ')
try:
    nb_of_elements = int(nb_of_elements)
except ValueError:
    print('Input is not an integer, giving up.')
    exit()
if nb_of_elements <= 0:
    print('Input should be striclty positive, giving up.')
    exit()
L = [randint(0, 19) for _ in range(nb_of_elements)]
print('The list is:' , L)
less_than_5 = 0        
between_5_and_9 = 0
between_10_and_14 = 0
between_15_and_19 = 0
for i in range(nb_of_elements):
    if L[i] < 5:
        less_than_5 += 1
    elif L[i] < 10:
        between_5_and_9 += 1
    elif L[i] < 15:
        between_10_and_14 += 1
    else:
        between_15_and_19 += 1
if less_than_5 < 2:
    print(' There is {} element less than 5.'.format(less_than_5))
else:
    print(' There are {} elements less than 5.'.format(less_than_5))
if between_5_and_9 < 2:
    print(' There is {} element between 5 and 9.'.format(between_5_and_9))
else:
    print(' There are {} elements between 5 and 9.'.format(between_5_and_9))
if between_10_and_14 < 2:
    print(' There is {} element between 10 and 14.'.format(between_10_and_14))
else:
    print(' There are {} elements between 10 and 14.'.format(between_10_and_14))
if between_15_and_19 < 2:
    print(' There is {} element between 15 and 19.'.format(between_15_and_19))
else:
    print(' There are {} elements between 15 and 19.'.format(between_15_and_19))

# Implements a function to encode a single strictly positive natural number that in base 2,
# reads as b_1 ... b_n, as b_1b_1 ... b_nb_n, and to encode a sequence of strictly positive
# natural numbers N_1 ... N_k with k >= 2 as N_1* 0 ... 0 N_k* where for all 0 < i <= k,
# N_i* is the encoding of N_i.
# Implements a function to decode a natural number N into a sequence of (one or more)
# strictly positive natural numbers according to the previous encoding scheme,
# or return None in case N does not encode such a sequence.
# Prompts the user to enter a strictly positive natural number, applies the decoding function,
# and prints out base 2 representations of both the encoding number and the decoded sequence
# for verification purposes.
#
# Written by *** and Eric Martin for COMP9021

import sys
import re


def encode(*integers):
    return int('0'.join(''.join(c + c for c in bin(i)[2: ]) for i in integers), 2)

# TODO learn how to test better
# TODO manually run through all the test cases
def decode(value):
    # return bin string without first two characters
    value = bin(value)[2:]

    # change values to a and b, just coz it works
    value = re.sub('00', 'a', value)
    value = re.sub('11', 'b', value)

    search_this = re.compile('1')
    found_this = re.split(search_this, value)
    if len(found_this) > 1:
        return
        # incorrect sequence

    search_this = re.compile('0')
    found_this = re.split(search_this, value)

    i = 0
    while i < len(found_this):
        found_this[i] = re.sub('a', '0', found_this[i])
        found_this[i] = re.sub('b', '1', found_this[i])
        i += 1

    # change from binary to decimal
    # value = int(value, 2)  # Convert a binary string to a decimal int.
    i = 0
    while i < len(found_this):
        found_this[i] = int(found_this[i], 2)
        i += 1

    return found_this





# input a number
# input an encoding
integer = input('Input a strictly positive integer: ')
if integer[0] == '0' or not integer.isdigit():
    print('Incorrect input, giving up!')
    sys.exit()
integer = int(integer)
#encoding = encode(integer)  # 1, 12)
#print('This encodes to: ', encoding)
decoding = decode(integer)
# encoding = encode(*decoding) #1, 12)
if decoding is None:
    print('Incorrect encoding!')
else:
    print('This encodes: ', decoding)
    # print('This encodes to: ', encoding)
    # print('This decodes to: ', decoding)
    print('Checking: ')
    print('  In base 2, {0} is {1}'.format(integer, bin(integer)[2:]))
    # print('  In base 2, {0} is {1}'.format(integer, bin(integer)[2: ]))
    # print('  In base 2, {0} is {1}'.format(encoding, bin(encoding)[2: ]))
    print('  In base 2, {0} is: [{1}]'.format(decoding, ', '.join(bin(i)[2:] for i in decoding)))
                


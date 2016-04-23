#Prompts the user to input the digits 1 to 8 (with possibly whitespace inserted anywhere),
#  in some order, say d1 d2 d3 d4 d5 d6 d7 d8, without repetition;
#  if the input is incorrect, then the program outputs an error message and exits.
# by Jordan Stewart, z3291315

import sys
import re
from collections import deque

# TODO make faster
# I might use collection.deque to deque the closest one
# I might check three nodes at a time
def calculate_number_of_steps(rectangle):
    step = 0
    step_position = 8
    patterns = [['1','2','3','4','5','6','7','8', step]]
    while True:
        pattern=patterns[0]
        print(pattern)

        # spawn three permutations each pattern
        patterns.append(row_exchange(pattern))
        patterns.append(right_shift(pattern))
        patterns.append(middle_clockwise_rotation(pattern))
        if ( match_pattern(pattern, rectangle) ):
            return pattern[step_position]


def calculate_number_of_steps_deque(rectangle):
    step = 0
    step_position = 8
    patterns = deque([['1','2','3','4','5','6','7','8', step]])
    while True:
        print(patterns[0])
        if match_pattern_deque(patterns[0], rectangle):
                return patterns[0][step_position]

        print(patterns[0])
        # spawn three permutations each pattern
        patterns.append(row_exchange(patterns[0]))
        patterns.append(right_shift(patterns[0]))
        patterns.append(middle_clockwise_rotation(patterns[0]))
        #pattern = patterns.popleft()
        print(patterns[0])
        patterns.popleft()
        print(patterns[0])
        #print(pattern)



def match_pattern_deque(pattern, rectangle):
    if pattern != rectangle:
        return False
    return True



def match_pattern(pattern, rectangle):
    # delete step variable in list
    temp = pattern
    if pattern == rectangle:
        pattern.append(temp)
        return True
    else:
        pattern.append(temp)
        return False



def row_exchange(pattern):
    # actually [8,7,6,5,4,3,2,1] or as input 87654321
    order=[7,6,5,4,3,2,1,0,8]
    pattern = [ pattern[j] for j in order]
    pattern=add_step(pattern[8])
    return pattern


def right_shift(pattern):
    # actually [4,1,2,3,6,7,8,5] or as input 41236785
    order=[3,0,1,2,5,6,7,4,8]
    pattern = [ pattern[j] for j in order]
    pattern=add_step(pattern[8])
    return pattern


def middle_clockwise_rotation(pattern):
    # actually [1,7,2,4,5,3,6,8] or as input 17245368
    order = [0,6,1,3,4,2,5,7,8]
    pattern = [ pattern[j] for j in order]
    pattern = add_step(pattern[8])
    return pattern


def add_step(step):
    step += 1
    return step


try:
    line = input('Input final configuration : ')
    line = re.sub('\s+', '', line) # remove possible whitespace
    line = list(line)   # make into a list of characters
    # TODO I should check if the values input are numbers
    if len(line)!=8:
        raise ValueError
    for i in line:
        int(i)      # gives up if not an int
    if not(''.join(sorted(line)) == '12345678'):
        raise ValueError
except ValueError:
    print('Incorrect input, giving up...')
    sys.exit()

#value = calculate_number_of_steps_deque(line)
value = calculate_number_of_steps(line)
print(value, 'steps are needed to reach the final configuration.')
# collections.deque nah

# check if a letter is added
#try:
#   val = int(userInput)
#except ValueError:
#   print("That's not an int!")
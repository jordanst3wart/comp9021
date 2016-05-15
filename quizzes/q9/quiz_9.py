# Randomly generates a binary search tree whose number of nodes
# is determined by user input, with node values ranging between 0 and 999,999,
# displays it, and outputs the sum of the node values on the longest branches,
# either counting the values for a given node only once,
# or counting it for as many times as the number of branches on which the node occurs.
#
# Written by Jordan Stewart and Eric Martin for COMP9021

import sys
from random import seed, randrange
from binary_tree import *


def sums_on_longest_branches(tree):
    return sum_branch((highest_branches(tree,tree.height())))


# vals is a list of lists for the highest branches
def sum_branch(vals):
    # sum unique vals, sum all vals
    print(vals)
    return sum(set(vals)), sum(vals)


# returns the highest branches as a list
def highest_branches(tree,height):
    # if nonething is here
    if tree.value is None:
        return [0]
    val = [tree.value]
    # no elements below
    if height == 0:
        return val
    # do I deal with the current value if height != 0
    val = branch(val,tree.left_node,height-1)  # I think i might need to pass it val to get it in the branch
    val.append(branch(val,tree.right_node,height-1))
    # if a valid branch it should append it
    val = flatten(val)
    return val


# returns a list
def branch(val,tree,height):
    if tree.height() == height:
        return val.append(highest_branches(tree,height)) # appends val if the sub tree is valid
    return [0] # end of the line


# flatten lists
# http://stackoverflow.com/questions/35415797/flatten-an-irregular-list-of-lists-in-python-recursively
def flatten(aList):
    t = []
    for i in aList:
        if not isinstance(i, list):
            t.append(i)
        else:
            t.extend(flatten(i))
    return t


provided_input = input('Enter two integers, the second one being positive: ')
provided_input = provided_input.split()
if len(provided_input) != 2:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    seed_arg = int(provided_input[0])
    nb_of_nodes = int(provided_input[1])
    if nb_of_nodes < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
 
seed(seed_arg)
tree = BinaryTree()
for _ in range(nb_of_nodes):
    datum = randrange(1000000)
    tree.insert_in_bst(datum)
print('Here is the tree that has been generated:')
tree.print_binary_tree()
print('The sums of the values on the longest branches are, counting each value only once')
print('  or counting it for all branches on which its occurs: ', end = '')
print(sums_on_longest_branches(tree))



# returns the highest branches in a list
def get_highest_branches_old(tree,height,vals):
    if tree.value is None:
        return 0
    if height == 0:
        return tree.value
    #vals.append(tree.value) #[[tree.value],[tree.value]]
    # repeats should create function
    if tree.left_node.height() == height - 1:
        #vals.append(list(tree.value))
        #vals.append(get_highest_branches(tree.left_node,height-1))
        vals.append(get_highest_branches(tree.left_node,height-1,vals))
    print(vals, "this is after left node finishes")
    if tree.right_node.height() == height - 1:
        vals.append(get_highest_branches(tree.right_node,height-1,vals))
        #vals[1].append(get_highest_branches(tree.right_node,height-1))
    print(vals, "this happened")
    return vals
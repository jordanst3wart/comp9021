# Prompts the user for a seed, a dimension dim, and an upper bound N.
# Randomly fills a grid of size dim x dim with numbers between 0 and N and computes:
# - the largest value n such that there is a path of the form (0, 1, 2,... n), and
# - the number of such paths.
# A path is obtained by repeatedly moving in the grid one step north, south, west, or east.

# Written by Jordan Stewart z3291315 and Eric Martin for COMP9021


import sys
from random import seed, randint


# a square of numbers
class Grid:
    # initialises the grid
    def __init__(self, upper_bound, dim):
        self.upper_bound = upper_bound
        self.dim = dim
        self.matrix = [[randint(0, self.upper_bound) for _ in range(self.dim)] for _ in range(self.dim)]

    def tell_dim(self):
        return self.dim

    def tell_matrix(self):
        return self.matrix

    def display_grid(self):
        print('Here is the grid that has been generated:')
        width = len(str(self.upper_bound))
        for i in range(self.dim):
            print('    ', end = '')
            for j in range(self.dim):
                print('{0:{2}s}{1:{2}d}'.format(' ', self.matrix[i][j], width), end = '')
            print()
        print()


# ascending squences through grids
class Paths:
    def __init__(self, nb, val):
        self.nb = nb
        self.val = val

    def _max(self,max_val,max_nb):
        if max_val > self.val: self.val = max_val
        if max_nb > self.nb: self.nb = max_nb

    def provide_answer(self):
        if self.nb == 0:
            print('There is no 0 in the grid.')
        else:
            print('The longest paths made up of consecutive numbers starting from 0 go up to {}.'.format(self.val))
            if self.nb == 1:
                print('There is one such path.')
            else:
                print('There are', self.nb, 'such paths.')

    # returns max_value, nb_of_paths_of_max_value
    def longest_paths(self, matrix,dim): # value and number
        for i in range(dim):
            for j in range(dim):
                #print("i :",i,"j:",j)
                self.update(i,j,matrix, dim,0)  # starts search at 0
                j += 1
            i += 1

    def update(self,i,j,matrix,dim,val):
        #print("matrix value: ",matrix[i][j])
        if matrix[i][j] == val:
            sides = [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]
            # basically a depth first recursive search
            for side in sides:
                if side[0] >= 0 and side[1] >= 0  and side[0] < dim and side[1]<dim: # inside grid
                    #print("side i:",side[0],"side j:",side[1], "matrix value is: ",matrix[i][j], " cell testing val is : ",matrix[side[0]][side[1]] )
                    if matrix[side[0]][side[1]] == val + 1:
                        if val + 1 == self.val:
                            self.nb += 1
                            #print("Added!!!")
                        elif val + 1 > self.val:
                            self.nb = 1
                            self.val = val +1
                            #print("Reset!!!")
                        self.update(side[0],side[1],matrix,dim,val+1)


provided_input = input('Enter three nonnegative integers: ')
provided_input = provided_input.split()
if len(provided_input) != 3:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    provided_seed, diml, upper_bound = tuple(int(provided_input[i]) for i in range(3))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(provided_seed)         # provides an initial number for the starting sequence
grid = Grid(upper_bound, diml)
grid.display_grid()
paths = Paths(0,0) # no value and no paths
paths.longest_paths(grid.tell_matrix(),grid.tell_dim()) # value and number
paths.provide_answer()


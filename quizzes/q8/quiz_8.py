# Randomly fills a grid of size 7 x 7 with NE, SE, SW, NW,
# meant to represent North-East, South-East, North-West, South-West,
# respectively, and starting from the cell in the middle of the grid,
# determines, for each of the 4 corners of the grid, the preferred path amongst
# the shortest paths that reach that corner, if any. At a given cell, it is possible to move
# according to any of the 3 directions indicated by the value of the cell;
# e.g., from a cell storing NE, it is possible to move North-East, East, or North.
# At any given point, one prefers to move diagonally, then horizontally,
# and vertically as a last resort.
#
# Written by Jordan Stewart and Eric Martin for COMP9021


import sys
from random import seed, choice
#from array_queue import * #<- no


def display_grid():
    for i in range(dim):
        print('    ', end='')
        for j in range(dim):
            print(' ', grid[i][j], end = '')
        print()
    print()


# modified from http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
def preferred_paths_to_corners(corners,grid,dim):
    grid = create_graph(grid,dim)
    middle = [3,3] # find middle
    paths=[]
    for corner in corners:
        paths[corner] = shortest_path(grid, middle, corner) # ['A', 'C', 'F']
    return paths

#graph = {'A': set(['B', 'C']),
#         'B': set(['A', 'D', 'E']),
#         'C': set(['A', 'F']),
#         'D': set(['B']),
#         'E': set(['B', 'F']),
#         'F': set(['C', 'E'])}

def create_graph(grid,dim):
    graph = {}
    for i in range(dim):
        for j in range(dim):
            node = (i,j) # was grid[i][j]
            graph[node] = edges(node,grid,dim) # was wrapped in set
    return graph



# attraches edges to a node
def edges(tp,grid,dim):
    val = []
    val.append(tp[1])
    val.append(tp[0])
    hor = [1,0]
    ver = [0,1]
    if grid[val[0]][val[1]] == 'NE':
        nodes = [plustrc(val,hor),plustrc(val,ver),plustrc(plustrc(val,hor),ver)]
    elif grid[val[0]][val[1]] == 'SE':
        nodes = [plustrc(val,hor),substrc(val,ver),plustrc(val,substrc(hor,ver))]
    elif grid[val[0]][val[1]] == 'SW':
        nodes = [substrc(val,hor),substrc(val,ver),substrc(substrc(val,hor),ver)]
    else: #'NW'
        nodes = [substrc(val,hor),plustrc(val,ver),plustrc(substrc(val,hor),ver)]
    nodes = is_valid_idx(nodes,grid,dim)
    return nodes


def substrc(a,b):
    return [i - j for i, j in zip(a, b)]


def plustrc(a,b):
    return [i - j for i, j in zip(a, b)]


#checks if valid
def is_valid_idx(nodes,grid,dim):
    return_me = []
    for node in nodes:
        temp=remove(node,dim)
        if temp != None:
            return_me.append(temp)
    return tuple(return_me)


# return none is not valid
def remove(node,dim):
    if node[0] > dim or node[0] <0:
        return None
    if node[1] > dim or node[1] <0:
        return None
    return node


def bfs_paths(grid, middle, corner):
    queue = [(tuple(middle), [middle])]
    while queue:
        (vertex, path) = queue.pop(0)
        print(tuple(path))
        print(grid[vertex])
        for next in grid[vertex] - tuple(path):
            if next == corner:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

#list(bfs_paths(graph, 'A', 'F')) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]

def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None


try:
    seed_arg = int(input('Enter an integer: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
    
seed(seed_arg)
size = 3
dim = 2 * size + 1
grid = [[0] * dim for _ in range(dim)]
directions = 'NE', 'SE', 'SW', 'NW'

for i in range(dim):
    for j in range(dim):
        grid[i][j] = choice(directions)
print('Here is the grid that has been generated:')
display_grid()

corners = (0, 0), (dim - 1, 0), (dim - 1, dim - 1), (0, dim - 1)
paths = preferred_paths_to_corners(corners,grid, dim)
if not paths:
    print('There is no path to any corner')
    sys.exit()
for corner in corners:
    if corner not in paths:
        print('There is no path to {}'.format(corner))
    else:
        print('The preferred path to {} is:'.format(corner))
        print('  ', paths[corner])

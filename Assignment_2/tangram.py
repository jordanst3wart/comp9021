# by Jordan Stewart
# Worse is better

import re

# 1. is input valid
# 2. two files are identical
# 3. are a solution to a tangram puzzle


class Tangram():
    pass


# available_coloured_pieces(file)


# open for xml types might not be defined
# opens the file, I might not need to write this
# def open(’pieces_AA.xml’)


# return true if valid pieces
def are_valid(coloured_pieces):
    return True


def available_coloured_pieces(file):
    # I would like to map
    pieces=list(map(parse_xml,file))
    return pieces # should return pieces

# input could be file but the file should be iterateable
# returns pieces
def parse_xml(line):
    line=re.split('\"',line)
    line=line[1].split()
    # M is the start, x,y L, and z is the end



# classes??
# point??
# line??
# piece??










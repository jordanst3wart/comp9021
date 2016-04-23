# Need to change to Python 3.5 from 2 something
# python does support object orientated programming very well
# the 2 to 3 upgrade made it less useable.

import functools


name_lengths = list(map(len, ["Mary", "Isla", "Sam"]))

print(name_lengths)


squares = list(map(lambda x: x ** 2, [0, 1, 2, 3, 4]))

print(squares)


names = ['Mary', 'Isla', 'Sam']

#for i in range(len(names)):
#    names[i] = hash(names[i])

names = list(map(hash, ['Mary', 'Isla', 'Sam']))

print(names)
# => [6306819796133686941, 8135353348168144921, -1228887169324443034]

#!/usr/bin/env python

import numpy as np
import sys

puzzle = [list(x.lower().strip()) for x in sys.stdin.readlines()]                                             # give in string form, separated by '\n'
puzzle = np.array(puzzle)
puzzle = np.char.upper(puzzle)

outcome = sys.argv[1].replace('array', 'np.array')
outcome = eval(outcome)

spaces = np.array(list(' ' * len(puzzle.ravel())))
spaces = spaces.reshape(puzzle.shape)
puzzle_out = np.char.add(np.char.add(spaces, puzzle), spaces)

for word in outcome:
    puzzle_out[outcome[word]] = ['[' + x + ']' for x in word]

print(puzzle_out)
print()

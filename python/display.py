#!/usr/bin/env python

import numpy as np
import sys

debug = eval(sys.argv[1])

puzzle = [list(x.lower().strip()) for x in sys.stdin.readlines()]
if debug: sys.stderr.write(repr(puzzle) + '\n')
puzzle = np.array(puzzle)
puzzle = np.char.upper(puzzle)
if debug: sys.stderr.write(repr(puzzle) + '\n')

outcome = sys.argv[2].replace('array', 'np.array')
if debug: sys.stderr.write(repr(outcome) + '\n')
outcome = eval(outcome)
if debug: sys.stderr.write(repr(outcome) + '\n')

spaces = np.array(list(' ' * len(puzzle.ravel())))
spaces = spaces.reshape(puzzle.shape)
puzzle_out = np.char.add(np.char.add(spaces, puzzle), spaces)
if debug: sys.stderr.write(repr(puzzle_out) + '\n')

for word in outcome:
    if debug: sys.stderr.write('\n'.join([repr(word), repr(outcome[word])]) + '\n')
    if debug: sys.stderr.write(repr(puzzle_out[outcome[word]]))
    puzzle_out[outcome[word]] = ['[' + x + ']' for x in word]

print(puzzle_out)
print()

#    for x in range(len(word)):
#        puzzle_out[outcome[word][1,x],outcome[word][0,x]] = '[' + word[x] + ']'

#!/usr/bin/env python

import numpy as np
import sys

debug = False
words = sys.argv[1::]                                                                                         # may be subject to change

directions = np.array([[[x, y] for y in range(-1, 2)] for x in range(-1, 2)]).ravel().reshape((9, 2))
if debug: print(directions)

# Defining the Puzzle
puzzle = [list(x.lower().strip()) for x in sys.stdin.readlines()]                                             # give in string form, separated by '\n'
puzzle = np.array(puzzle)
puzzle = np.char.upper(puzzle)
if debug: print(puzzle)

# Finding Words

solution = {}

for word in words:
    word = word.upper()
    start = np.array(np.where(puzzle == word[0]))
    if debug: print(start, start + directions[0].reshape(2,1), sep='\n')

    outcome = []

    for direction in directions:
        direction = direction.reshape(2, 1)
        ins = np.array([start + (direction * x) for x in range(len(word))])
        outs = np.array([puzzle[tuple(ind % 12)] for ind in ins])
        if debug: print(ins, outs, sep='\n\n', end='\n\n\n')
        if debug: print()
        for x in range(len(outs[0])):
            out = ''.join(outs[:,x])
            if out == word:
                if debug: print(out, x)
                if debug: print(ins)
                outcome = [ins[:,0,x], ins[:,1,x]] # Row 0 = Y; Row 1 = X
                break

    solution[word] = outcome

print(solution)
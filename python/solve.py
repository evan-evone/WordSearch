#!/usr/bin/env python

import numpy as np
import sys

debug = eval(sys.argv[1])
words = sys.argv[2::]

directions = np.array([[x, y] for y in range(-1, 2) for x in range(-1, 2)])
if debug: sys.stderr.write(repr(directions) + '\n')

# Defining the Puzzle
lines = sys.stdin.readlines()
if debug: sys.stderr.write(repr(lines) + '\n')
puzzle = [list(x.lower().strip()) for x in lines]
if debug: sys.stderr.write(repr(puzzle) + '\n')
puzzle = np.char.upper(np.array(puzzle))
if debug: sys.stderr.write(repr(puzzle) + '\n')

# Finding Words

solution = {}

for word in words:
    word = word.upper()
    start = np.array(np.where(puzzle == word[0]))
    if debug: sys.stderr.write('\n'.join([repr(start), repr(start + directions[0].reshape(2,1))]) + '\n')

    outcome = []

    for direction in directions:
        direction = direction.reshape(2, 1)
        ins = np.array([start + (direction * x) for x in range(len(word))])
        outs = np.array([puzzle[tuple(ind % 12)] for ind in ins])
        if debug: sys.stderr.write('\n\n'.join([repr(ins), repr(outs)]) + '\n\n\n')
        if debug: sys.stderr.write('\n')
        for x in range(len(outs[0])):
            out = ''.join(outs[:,x])
            if out == word:
                if debug: sys.stderr.write('\n'.join([repr(out), repr(x)]) + '\n')
                if debug: sys.stderr.write(repr(ins) + '\n')
                outcome = [ins[:,0,x], ins[:,1,x]] # Row 0 = Y; Row 1 = X
                break

    solution[word] = outcome

print(solution)

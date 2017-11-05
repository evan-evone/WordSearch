#!/usr/bin/env python

# Prerequisites
from sys import argv
import numpy as np

argv = argv[1:]
if '-d' in argv: debug = True; argv.remove('-db')
else: debug = False
wsName = argv[0]
words = argv[1:]

directions = np.array([[[x, y] for y in range(-1, 2)] for x in range(-1, 2)]).ravel().reshape((9, 2))
if debug: print(directions)

# Defining the Puzzle
wordSearch = open(wsName, 'r')
lines = [list(x.lower().strip()) for x in wordSearch.readlines()]
wordSearch.close()
puzzle = np.array(lines)
puzzle = np.char.upper(puzzle)
if debug: print(puzzle)

# Finding Words
word = words[0].upper()
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
            print(ins)
            outcome = [ins[:,0,x], ins[:,1,x]]
            break

print(outcome)
print(puzzle[outcome])

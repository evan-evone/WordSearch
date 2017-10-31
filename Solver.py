#!/usr/bin/env python

  #Getting Information from System
from Board import textBoard
from sys import argv
wsNm = argv[1]
slNm = argv[2]


  #Defining the Puzzle
lines = []

wordSearch = open(wsNm, 'r')
for line in wordSearch:
	lines.append(line.lower())
wordSearch.close()

width = len(lines[0]) - 1
height = len(lines)
max = 0
if width > height:
	max = width
else:
	max = height

puzzle = textBoard(' ', width, height)

for n, l in enumerate(lines):
	lines[n] = list(l[0:width:1])
	puzzle[n] = list(''.join(lines[n]))

for n, l in enumerate(lines):
	for y, x in enumerate(lines[n]):
		lines[n][y] = ' ' + x + ' '

puzzle.represent = lines

  #Solving puzzle

words = argv[3::]
wordsDic = {}

for w in words:
	found = puzzle.find(w)
	if found[0]:
		wordsDic[w] = found[1]
		puzzle.show(w)

print()

solution = open(slNm, 'r+')

for w in wordsDic:
	solution.write('{:10s}'.format(w) + ' : ' + str(wordsDic[w]) + '\n')
	print('{:10s}'.format(w) + ' : ' + str(wordsDic[w]))

solution.close()
print()
puzzle.showBoard()

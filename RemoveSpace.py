#!/usr/bin/env python

from sys import argv
file = open(argv[1], 'r+')

lines = []
for line in file:
	lines.append(line)

str = ''

for num, line in enumerate(lines):
	newline = [x for x in list(line) if x != ' ']
	for char in newline:
		str += char
	lines[num] = str

str = str.lower()

file.close()

file = open(argv[1], 'w')

print(str)
file.write(str)

file.close()

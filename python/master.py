#!/usr/bin/env python

import argparse
import sys
import os

# Determine variables/arguments
parser = argparse.ArgumentParser(description='WordSearch arguments')
parser.add_argument('-d', action='store_true',
                    help='enable debug mode (frequent mid-execution printing)')

parser.add_argument('-f', metavar='INFILE', nargs='?', const='-', default='-',
                    help='specify input file (default -, stdin)')
parser.add_argument('-o', metavar='OUTFILE', nargs='?', const='-', default='-',
                    help='specify output file (default -, stdout)')
parser.add_argument('-s', metavar='SOLUTION', nargs='?', const='-', default='',
                    help='specify file to output solution (default none).\
                          if no argument is specified, prints to -, stdout')
parser.add_argument('-w', metavar='WORDFILE',
                    help='specify file from which words should be read.\
                          by default, words are read only from arguments list.')

parser.add_argument('words', nargs='*', default=[],
                    help='words to search for in addition to word_file words')

args = vars(parser.parse_args())
if args['d']: sys.stderr.write(repr(args) + '\n')

# Get real path to source directory
script_path = os.path.realpath(__file__)
exec_dir = '/'.join(script_path.split('/')[:-1])
if args['d']: sys.stderr.write(repr(exec_dir) + '\n')

# Get Puzzle
if args['f'] == '-':
    puzzle = sys.stdin.readlines()
else:
    puzzle_file = open(args['f'], 'r')
    puzzle = [x.lower().strip() for x in puzzle_file.readlines()]
    puzzle_file.close()
if args['d']: sys.stderr.write(repr(puzzle) + '\n')

# Get Words
words = args['words']
if args['w'] != None:
    words_file = open(args['w'], 'r')
    words += [x.lower().strip() for x in words_file.readlines()]
    words_file.close()

if args['d']: sys.stderr.write(repr(words) + '\n')

# Get Solution/Display
solution = os.popen('echo "{puzzle}" | {path}/solve.py {debug} {words}'.format(
    puzzle='\n'.join(puzzle),
    path=exec_dir,
    debug=args['d'],
    words=' '.join(words)
)).read()
if args['d']: sys.stderr.write(repr(solution) + '\n')

if args['d']: sys.stderr.write('\n\n\n\n')

display = os.popen('echo "{puzzle}" | {path}/display.py {debug} "{solution}"'.format(
    puzzle='\n'.join(puzzle),
    path=exec_dir,
    debug=args['d'],
    solution=solution
)).read()
if args['d']: sys.stderr.write(repr(solution) + '\n')

# Display Solution
if args['o'] == '-':
    print(display)
else:
    outfile = open(args['o'], 'w')
    outfile.truncate(0)
    outfile.write(display)
    outfile.close()

if args['s'] != '':
    if args['s'] == '-':
        print(solution)
    else:
        outfile = open(args['s'], 'w')
        outfile.truncate(0)
        outfile.write(solution)
        outfile.close()

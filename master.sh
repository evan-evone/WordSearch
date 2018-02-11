#!/usr/bin/env bash

# please note that this is temporary
# this is meant to save the proper calling syntax
# therefore calls are limited to two arguments: string of words and filename

output=$(python/solve.py $1 < $2)                                                                             # $1 = string of args, separated by spaces. `sys.argv`
python/display.py "$output" < $2                                                                              # $2 = string/file of wordsearch. `sys.stdin`

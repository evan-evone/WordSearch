#!/usr/bin/env python

from sys import stdin
string = ''.join([x for x in stdin.read() if x != ' ']).replace('\\n', '\n').upper()
print(string)

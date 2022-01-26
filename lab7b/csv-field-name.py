#!/usr/bin/env python3

#LatD,LatM,LatS,NS,LonD,LonM,LonS,EW,City,State
#               | |
#               i j
import sys

args = sys.argv[1]
s = input()
i = 0
pos = 0
while pos < int(args):
    if s[i] == ",":
        pos = pos + 1
    i = i + 1
j = i
while j < len(s) and s[j] != ",":
    j = j + 1
print(s[i:j])

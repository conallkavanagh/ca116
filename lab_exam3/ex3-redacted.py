#!/usr/bin/env python3

import sys

blacklist = {}
with open("banned.txt") as f:
    i = 0
    line = f.readline().rstrip()
    while len(line) > 0:
        blacklist[line] = True
        line = f.readline().rstrip()

s = sys.stdin.readlines()
i = 0
while i < len(s):
    curr_line = s[i].rstrip().split()
    j = 0
    while j < len(curr_line):
        if curr_line[j] in blacklist:
            curr_line[j] = "*" * len(curr_line[j])
        j = j + 1
    print(" ".join(curr_line))
    i = i + 1

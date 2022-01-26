#!/usr/bin/env python3

import sys

s = sys.stdin.readlines()
i = 0
while i < len(s):
    s[i] = s[i].split()[1] + " " + s[i].split()[0]
    i = i + 1

j = 0
while j < len(s):
    i = j
    minimum = s[i]
    pos = i
    while i < len(s):
        if s[i] < minimum:
            minimum = s[i]
            pos = i
        i = i + 1
    tmp = s[j]
    s[j] = s[pos]
    s[pos] = tmp
    j = j + 1

i = 0
while i < len(s):
    print(s[i].split()[1] + " " + s[i].split()[0])
    i = i + 1

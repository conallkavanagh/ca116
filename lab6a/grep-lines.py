#!/usr/bin/env python3

import sys

pattern = sys.argv[1]
s = input()
l = []
while s != "end":
    i = 0
    while i < len(s):
        if s[i:len(pattern) + i] == pattern:
            l.append(s)
        i = i + 1
    s = input()

i = 0
while i < len(l):
    print(l[i])
    i += 1

#!/usr/bin/env python3

import sys

s = sys.stdin.readlines()
i = 0
points = {}
while i < len(s):
    point = "-".join(s[i].rstrip().split())
    points[point] = True
    i = i + 1

print(" " + "-" * 20)
y = 0
while y < 20:
    x = 0
    line = "|"
    while x < 20:
        if str(x) + "-" + str(20 - y - 1) in points:
            line = line + "*"
        else:
            line = line + " "
        x = x + 1
    line = line + "|"
    print(line)
    y = y + 1
print(" " + "-" * 20)

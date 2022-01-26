#!/usr/bin/env python3

s = input()
lines = []
while s != "end":
    lines.append(s)
    s = input()
day = input()
i = 0
while i < len(lines):
    line = lines[i]
    if line[0] == day:
        print(line)
    i = i + 1

#!/usr/bin/env python3

import sys

s = " ".join(sys.stdin.read().split())
lines = []

i = 0
p = 0
while i < len(s):
    if s[i:i + 2] == ". " or s[i:i + 2] == "! " or s[i:i + 2] == "? ":
        curr_line = s[p:i + 1].lstrip()
        lines.append(curr_line[0].capitalize() + curr_line[1:])
        p = i + 1
    elif i == len(s) - 1:
        curr_line = s[p:i + 1].lstrip()
        lines.append(curr_line[0].capitalize() + curr_line[1:])
    i = i + 1
print("\n".join(lines))

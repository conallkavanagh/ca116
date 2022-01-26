#!/usr/bin/env python3

import sys

s = " ".join(sys.stdin.read().split())
lines = []

i = 0
p = 0
while i < len(s):
    if s[i:i + 2] == ". " or s[i:i + 2] == "! " or s[i:i + 2] == "? ":
        lines.append(s[p:i + 1].lstrip())
        p = i + 1
    elif i == len(s) - 1:
        lines.append(s[p:i + 1].lstrip())
    i = i + 1

print("\n".join(lines))

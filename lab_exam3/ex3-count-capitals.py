#!/usr/bin/env python3

import sys

s = sys.stdin.read().rstrip()
i = 0
total = 0
while i < len(s):
    if s[i] >= "A" and s[i] <= "Z":
        total = total + 1
    i = i + 1
print(total)

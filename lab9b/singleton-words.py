#!/usr/bin/env python3

import sys

s = sys.stdin.readlines()
words = {}
i = 0
while i < len(s):
    words[s[i].rstrip()] = s[i].rstrip() not in words
    i = i + 1

for k in words:
    if words[k]:
        print(k)

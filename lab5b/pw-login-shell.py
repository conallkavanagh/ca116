#!/usr/bin/env python3

s = ""

while s != "end":
    s = input()
    i = 0
    while i < len(s) and s[i] != ":":
        i = i + 1
    j = len(s) - 1
    while j > 0 and s[j] != ":":
        j = j - 1
    if s != "end":
        print(s[:i] + " " + s[j + 1:])

#!/usr/bin/env python3

s = ""

while s != "end":
    s = input()
    i = 0
    while i < len(s) and s[i] != ":":
        i = i + 1
    if s != "end":
        print(s[:i])

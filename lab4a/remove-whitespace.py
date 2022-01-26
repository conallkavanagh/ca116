#!/usr/bin/env python3

s = input()
i = 0
n = len(s)
s2 = ""

while i < n:
    if s[i] != " ":
        s2 = s2 + s[i]
    i = i + 1
print(s2)

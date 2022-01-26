#!/usr/bin/env python3

s = ""
total = 0

while s != "end":
    s = input()
    i = 0
    x = 0
    while i < len(s) and s[x + 1:x + 3] != "WI":
        if s[i] == ",":
            x = i
        if s[x + 1:x + 3] == "WI":
            total = total + 1
        i = i + 1
print(total)

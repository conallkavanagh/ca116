#!/usr/bin/env python3

s = input()

while s != "end":
    s = input()
    i = 0
    x = 0
    while i < len(s) and s[x - 4:x] != "City":
        if s[i] == ",":
            x = i
        if s[x - 4:x] == "City":
            print(s[:x])
        i = i + 1

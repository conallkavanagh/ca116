#!/usr/bin/env python3

s = input()
i = 0

while i < len(s):
    new_s = ""
    while i < len(s) and s[i] != ",":
        new_s = new_s + s[i]
        i = i + 1
    print(new_s)
    i = i + 1

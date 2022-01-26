#!/usr/bin/env python3

s = input()
while s != "end":
    s = s.split()
    print(" ".join(s[5:]))
    s = input()

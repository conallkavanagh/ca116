#!/usr/bin/env python3

s = input()
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
i = 0

while i < len(s):
    j = 0
    while j < len(upper):
        if upper[j] == s[i]:
            print(i)
            i = len(s)
            j = len(upper)
        j = j + 1
    i = i + 1

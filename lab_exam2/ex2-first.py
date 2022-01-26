#!/usr/bin/env python3

s = input()
i = 0
while i < len(s) and (s[i] > "9" or s[i] < "0"):
    i = i + 1
if i < len(s):
    print(s[i])

#!/usr/bin/env python3

s = input()
i = 0
total = 0
while i < len(s):
    total = total + int(s[i])
    i = i + 1
print(total)

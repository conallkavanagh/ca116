#!/usr/bin/env python3

s = input()
total = 0

while s != "end":
    i = 0
    while i < len(s) and s[len(s) - i - 1] != "y":
        i = i + 1
    n = len(s) - i
    if s[n + 1:] == "correct":
        total += 1
    s = input()
print(total)

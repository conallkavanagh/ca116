#!/usr/bin/env python3

s = input()
reverse = ""
i = 0
n = len(s)

while i < n:
    reverse = reverse + s[n - i - 1]
    i = i + 1
print(reverse)

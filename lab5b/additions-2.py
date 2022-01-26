#!/usr/bin/env python3

i = 0
s = input()
total = 0
j = 0
k = 0
while i < 5:
    while j < len(s) and s[j] != "+":
        j = j + 1
    total = total + int(s[k:j])
    k = j + 1
    j = k
    i = i + 1
print(total)

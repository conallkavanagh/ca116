#!/usr/bin/env python3

i = 0
n = int(input())
total = n
while i < 9:
    n = int(input())
    if total < n:
        total = n
    i = i + 1
print(total)

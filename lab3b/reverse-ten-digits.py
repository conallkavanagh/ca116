#!/usr/bin/env python3

i = 0
j = 0
total = 0
while i < 10:
    n = int(input())
    total = total + n * 10 ** (9 - i)
    i = i + 1

while j < 10:
    print(total % (10 ** (j + 1)) // 10 ** j)
    j = j + 1

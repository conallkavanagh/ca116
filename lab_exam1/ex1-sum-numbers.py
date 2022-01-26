#!/usr/bin/env python3

n = int(input())
i = 0
total = 0
while i < n:
    num = input()
    if num == "one":
        num = 1
    elif num == "two":
        num = 2
    elif num == "three":
        num = 3
    elif num == "four":
        num = 4
    else:
        num = 5
    total = total + num
    i = i + 1
print(total)

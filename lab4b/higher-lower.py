#!/usr/bin/env python3

i = 0
n = int(input())

while i < 5:
    n2 = int(input())
    if n2 > n:
        print("higher")
    elif n2 < n:
        print("lower")
    else:
        print("equal")
    n = n2
    i = i + 1

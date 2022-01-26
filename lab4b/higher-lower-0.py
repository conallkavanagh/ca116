#!/usr/bin/env python3

n = int(input())

while n != 0:
    n2 = int(input())
    if n2 > n and n2 != 0:
        print("higher")
    elif n2 < n and n2 != 0:
        print("lower")
    elif n2 == n:
        print("equal")
    n = n2

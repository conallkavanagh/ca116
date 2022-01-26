#!/usr/bin/env python3

n = int(input())
x = 0
y = 1
z = 0
while x < n:
    print(x)
    z = x
    x = x + y
    y = z

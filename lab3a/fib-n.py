#!/usr/bin/env python3

i = 0
n = int(input())
x = 0
y = 1
z = 0
while i < n:
    print(x)
    z = x
    x = x + y
    y = z
    i = i + 1

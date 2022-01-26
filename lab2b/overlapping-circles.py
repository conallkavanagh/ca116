#!/usr/bin/env python3

x1 = int(input())
y1 = int(input())
r1 = int(input())
x2 = int(input())
y2 = int(input())
r2 = int(input())

a = x1 - x2
b = y1 - y2
h = a * a + b * b #== (distance between 2 centres) ** 2
r = (r1 + r2) ** 2 #== (sum of both radii) ** 2

if h < r:
    print("yes")
else:
    print("no")

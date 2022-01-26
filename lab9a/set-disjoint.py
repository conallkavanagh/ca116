#!/usr/bin/env python3

with open("a.txt") as f:
    a = f.readlines()
with open("b.txt") as f:
    b = f.readlines()

seen = {}
i = 0
while i < len(a):
    seen[a[i].rstrip()] = True
    i += 1
i = 0
while i < len(b) and b[i].rstrip() not in seen:
    i += 1
if i < len(b):
    intersect = True
else:
    intersect = False
if intersect:
    print("intersecting")
else:
    print("disjoint")

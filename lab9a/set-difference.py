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
while i < len(b):
    if b[i].rstrip() in seen:
        seen[b[i].rstrip()] = False
    i += 1
for k in seen:
    if seen[k]:
        print(k)

#!/usr/bin/env python3

a = []
s = input()
while s != "end":
    a.append(int(s))
    s = input()
b = []
s = input()
while s != "end":
    b.append(int(s))
    s = input()

i = 0
j = 0
c = []
while i < len(a) or j < len(b):
    if i < len(a) and j < len(b) and a[i] < b[j]:
        c.append(a[i])
        i = i + 1
    elif j < len(b):
        c.append(b[j])
        j = j + 1
    else:
        c.append(a[i])
        i = i + 1

i = 0
while i < len(c):
    print(c[i])
    i = i + 1

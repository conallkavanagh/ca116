#!/usr/bin/env python3

s = input()
l = []

while s != "end":
    i = 0
    l.append(s)
    while i < len(l) - 1:
        if l[i] == s:
            l.pop()
        i += 1
    s = input()

i = 0
while i < len(l):
    print(l[i])
    i += 1

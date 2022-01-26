#!/usr/bin/env python3

s = input()
l = []

while s != "end":
    l.append(s)
    s = input()

i = 0
while i < len(l):
    print(l[len(l) - i - 1])
    i += 1

#!/usr/bin/env python3

s = input()
l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while s != "end":
    s = int(s)
    l[s] += 1
    s = input()

i = 0
while i < len(l):
    print(i, l[i] * "*")
    i += 1

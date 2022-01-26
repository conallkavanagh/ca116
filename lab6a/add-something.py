#!/usr/bin/env python3

m = []
s = input()

while s != "end":
    m.append(int(s))
    s = input()

n = int(input())
i = 0
while i < len(m):
    print(m[i] + n)
    i += 1

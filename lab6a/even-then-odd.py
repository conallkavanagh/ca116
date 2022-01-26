#!/usr/bin/env python3

s = input()
odd = []

while s != "end":
    s = int(s)
    if s % 2 == 0:
        print(s)
    else:
        odd.append(s)
    s = input()

i = 0
while i < len(odd):
    print(odd[i])
    i += 1

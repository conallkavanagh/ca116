#!/usr/bin/env python3

s = input()
strings = []
while s != "end":
    strings.append(s)
    s = input()

j = 0
while j < len(strings):
    i = j
    minimum = strings[i]
    pos = i
    while i < len(strings):
        if strings[i] < minimum:
            minimum = strings[i]
            pos = i
        i = i + 1
    tmp = strings[j]
    strings[j] = strings[pos]
    strings[pos] = tmp
    j = j + 1

i = 0
while i < len(strings):
    print(strings[i])
    i = i + 1

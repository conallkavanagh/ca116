#!/usr/bin/env python3

s = input()
while s != "end":
    tokens = s.split()
    hours = int(tokens[2])
    time = int(tokens[1])
    tokens[1] = str(time) + ":00"
    tokens[2] = str(time + hours - 1) + ":50"
    print(" ".join(tokens))
    s = input()

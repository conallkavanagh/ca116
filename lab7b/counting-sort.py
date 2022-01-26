#!/usr/bin/env python3

count = [0] * 1000
s = input()
while s != "end":
    count[int(s)] = count[int(s)] + 1
    s = input()
i = 0
output = ""
while i < 1000:
    if count[i] > 0:
        output = output + (str(i) + "\n") * count[i]
    i = i + 1
if len(output) > 0:
    output = output[:len(output) - 1]
    print(output)

#!/usr/bin/env python3

s = input()
csv = []
while s != "end":
    csv.append(s)
    s = input()
field = int(input())
i = 0
while i < len(csv):
    pos = 0
    start_pos = 0
    end_pos = 0
    while end_pos < len(csv[i]) and csv[i][end_pos] != ",":
        end_pos = end_pos + 1
    j = 0
    while j < len(csv[i]) and pos < field:
        if csv[i][j] == ",":
            pos += 1
            start_pos = j + 1
            end_pos = j + 2
            while end_pos < len(csv[i]) and csv[i][end_pos] != ",":
                end_pos += 1
        j = j + 1
    print(csv[i][start_pos:end_pos])
    i = i + 1

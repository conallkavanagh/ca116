#!/usr/bin/env python3

s = input()
dates = []
while s != "end":
    dates.append(s)
    s = input()
j = 0
while j < len(dates):
    i = j
    minimum = int(dates[i][6:8] + dates[i][3:5] + dates[i][0:2])
    pos = i
    while i < len(dates):
        if int(dates[i][6:8] + dates[i][3:5] + dates[i][0:2]) < minimum:
            minimum = int(dates[i][6:8] + dates[i][3:5] + dates[i][0:2])
            pos = i
        i = i + 1
    tmp = dates[j]
    dates[j] = dates[pos]
    dates[pos] = tmp
    j = j + 1
i = 0
while i < len(dates):
    print(dates[i][9:])
    i = i + 1

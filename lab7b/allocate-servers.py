#!/usr/bin/env python3

jobs = []
s = input()
time = 1000
while s != "end":
    jobs.append(int(s))
    s = input()
#calculate largest overlap
overlap = 0
i = 0
while i < len(jobs):
    tmp = 0
    j = i
    while j < len(jobs) and jobs[j] < jobs[i] + time:
        tmp = tmp + 1
        j = j + 1
    if overlap < tmp:
        overlap = tmp
    i = i + 1
print(overlap)

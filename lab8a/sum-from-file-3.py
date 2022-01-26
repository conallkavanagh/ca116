#!/usr/bin/env python3

import sys
file_name = sys.argv[1]
nums = []
with open(file_name) as f:
    currline = f.readline()
    while 0 < len(currline):
        i = 0
        currnums = currline.split()
        while i < len(currnums):
            nums.append(currnums[i])
            i = i + 1
        currline = f.readline()

i = 0
total = 0
while i < len(nums):
    total = total + int(nums[i])
    i = i + 1
print(total)

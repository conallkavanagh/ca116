#!/usr/bin/env python3

import sys
files = sys.argv[1:]
i = 0
nums = []
while i < len(files):
    with open(files[i]) as f:
        currline = f.readline()
        while 0 < len(currline):
            j = 0
            currnums = currline.split()
            while j < len(currnums):
                nums.append(currnums[j])
                j = j + 1
            currline = f.readline()
    i = i + 1

i = 0
total = 0
while i < len(nums):
    total = total + int(nums[i])
    i = i + 1
print(total)

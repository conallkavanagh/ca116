#!/usr/bin/env python3

import sys
args = sys.argv[1:]

nums = []
i = 0
while i < len(args):
    with open(args[i]) as f:
        line = f.readline().rstrip()
        while 0 < len(line):
            nums.append(int(line))
            line = f.readline().rstrip()
    i = i + 1

i = 0
total = 0
while i < len(nums):
    total = total + nums[i]
    i = i + 1
print(total)

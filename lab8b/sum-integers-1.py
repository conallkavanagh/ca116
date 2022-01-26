#!/usr/bin/env python3

import sys

nums = []
line = sys.stdin.readline().rstrip()
while 0 < len(line):
    nums.append(int(line))
    line = sys.stdin.readline().rstrip()

i = 0
total = 0
while i < len(nums):
    total = total + nums[i]
    i = i + 1
print(total)

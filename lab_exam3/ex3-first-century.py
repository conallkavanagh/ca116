#!/usr/bin/env python3

import sys

nums = sys.stdin.readlines()
i = 0
while i < len(nums) and int(nums[i].rstrip()) < 100:
    i = i + 1
if i < len(nums):
    print(nums[i].rstrip())
else:
    print("none")

#!/usr/bin/env python3

s = input()
nums = []
while s != "end":
    nums.append(int(s))
    s = input()
i = int(input())
minimum = nums[i]
pos = i
while i < len(nums):
    if nums[i] < minimum:
        minimum = nums[i]
        pos = i
    i = i + 1
print(pos)

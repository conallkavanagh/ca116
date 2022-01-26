#!/usr/bin/env python3

s = input()
nums = []
while s != "end":
    nums.append(int(s))
    s = input()

i = 0
minimum = nums[0]
pos = 0
while i < len(nums):
    if nums[i] < minimum:
        minimum = nums[i]
        pos = i
    i = i + 1
print(pos)

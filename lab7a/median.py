#!/usr/bin/env python3

s = input()
nums = []
while s != "end":
    nums.append(int(s))
    s = input()

j = 0
while j < len(nums):
    i = j
    minimum = nums[i]
    pos = i
    while i < len(nums):
        if nums[i] < minimum:
            minimum = nums[i]
            pos = i
        i = i + 1
    tmp = nums[j]
    nums[j] = nums[pos]
    nums[pos] = tmp
    j = j + 1

print(nums[len(nums) // 2])

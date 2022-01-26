#!/usr/bin/env python3

nums = []
i = 0
while i < 3:
    s = int(input())
    nums.append(s)
    i = i + 1

count = 0
while count != 0:
    j = 0
    while j < count:
        if nums[j] > nums[j + 1]:
            temp = nums[j]
            nums[j] = nums[j + 1]
            nums[j + 1] = temp
        j = j + 1
    count = count - 1

k = 0
while k < 3:
    print(nums[k])
    k = k + 1

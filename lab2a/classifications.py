#!/usr/bin/env python3

mark = int(input())

first = mark >= 70
second = 70 > mark >= 50
third = 50 > mark >= 40
fail = 40 > mark

print("first: " + str(first))
print("second: " + str(second))
print("third: " + str(third))
print("fail: " + str(fail))

#!/usr/bin/env python3

#A year is a leap year if:
#it is divisible by 400, or it is divisible by 4 but not by 100

year = int(input())

print(year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))

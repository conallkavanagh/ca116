#!/usr/bin/env python3

n = int(input())
digit = n % 10

if n == 11 or n == 12 or n == 13:
    print("th")
elif digit == 1:
    print("st")
elif digit == 2:
    print("nd")
elif digit == 3:
    print("rd")
else:
    print("th")

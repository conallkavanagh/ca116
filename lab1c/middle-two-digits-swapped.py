#!/usr/bin/env python3

num = int(input())

two_digits = (num % 10000) // 100
two_digits = (two_digits % 10) * 10 + (two_digits // 10)

print(two_digits)

#!/usr/bin/env python3

num = int(input())

two_digits = (num % 10000 - num % 100) // 100

print(two_digits)

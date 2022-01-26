#!/usr/bin/env python3

a = int(input())
b = int(input())
temp = 0

while b != 0:
    temp = a
    a = b
    b = temp % b
print(a)

#!/usr/bin/env python3

binary = str(input())
i = 0
dec = 0
n = len(binary)
while i < n:
    dec = dec + (2 ** i) * int(binary[n - i - 1])
    i = i + 1
print(dec)

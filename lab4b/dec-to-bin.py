#!/usr/bin/env python3

dec = int(input())
binary = ""

while dec != 0:
    rem = dec % 2
    binary = str(rem) + binary
    dec = dec // 2
print(binary)

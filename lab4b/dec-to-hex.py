#!/usr/bin/env python3

hex_digits = "0123456789abcdef"
dec = int(input())
hex = ""

while dec != 0:
    quotient = dec // 16
    rem = dec % 16
    hex = hex_digits[rem] + hex
    dec = quotient
print(hex)

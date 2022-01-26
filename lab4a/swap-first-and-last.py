#!/usr/bin/env python3

s = input()
swap = s[len(s) - 1] + s[1:len(s) - 1] + s[0]

print(swap)

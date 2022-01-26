#!/usr/bin/env python3

n = int(input())

if n % 2 == 0 and n != 2 or n == 1:
    print("not prime")
elif n % 3 == 0 and n != 3:
    print("not prime")
else:
    print("prime")

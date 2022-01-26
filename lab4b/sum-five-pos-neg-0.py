#!/usr/bin/env python3

n = int(input())
totalpos = 0
totalneg = 0

while n != 0:
    if n < 0:
        totalneg = totalneg + n
    else:
        totalpos = totalpos + n
    n = int(input())
print(str(totalneg) + " " + str(totalpos))

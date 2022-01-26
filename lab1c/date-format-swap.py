#!/usr/bin/env python3

swap = int(input())
swap = ((swap % 10000) - (swap % 100) + (swap // 10000)) * 100 + (swap % 100)

print(swap)

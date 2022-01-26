#!/usr/bin/env python3

if __name__ == "__main__":
    a = [49, 32, 39, 13, 30, 12, 14, 19, 31, 31]

i = 0
minim = a[0]
pos = 0
while i < len(a):
    if minim > a[i]:
        minim = a[i]
        pos = i
    i = i + 1
print(pos)

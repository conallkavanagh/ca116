#!/usr/bin/env python3

f = input()

i = 0
while f[i] != ".":
    i += 1

print(f[:i])
print(f[i + 1:])

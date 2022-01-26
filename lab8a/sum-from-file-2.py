#!/usr/bin/env python3

import sys
file_name = sys.argv[1]
with open(file_name) as f:
    lines = f.readlines()

i = 0
total = 0
while i < len(lines):
    total = total + int(lines[i])
    i = i + 1
print(total)

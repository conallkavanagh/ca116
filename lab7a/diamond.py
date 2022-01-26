#!/usr/bin/env python3

import sys

size = int(sys.argv[1])

i = 0
while i < size:
    if i <= size // 2:
        print(" " * (size // 2 - i) + "*" * (2 * (i + 1) - 1))
    else:
        print(" " * (i - size // 2) + "*" * (2 * (size - i) - 1))
    i = i + 1

#!/usr/bin/env python3

import sys

n = sys.argv[1]

inp = sys.stdin.readlines()
i = 0
while i < len(inp):
    if int(inp[i]) % (10 ** len(n)) != int(n):
        sys.stdout.write(inp[i])
    i = i + 1

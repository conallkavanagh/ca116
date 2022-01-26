#!/usr/bin/env python3

import sys
n = sys.argv[1:]
i = 0
while i < len(n):
    if int(n[i]) > 50:
        print(n[i])
    i = i + 1

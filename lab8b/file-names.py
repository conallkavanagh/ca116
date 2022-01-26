#!/usr/bin/env python3

import sys

files = sys.stdin.readlines()
i = 0
while i < len(files):
    f = files[i].split("/")
    print(f[len(f) - 1].rstrip())
    i = i + 1

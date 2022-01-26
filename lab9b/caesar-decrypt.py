#!/usr/bin/env python3

import sys
n = 13
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

src = lower[n:] + lower[:n] + upper[n:] + upper[:n]
dst = lower + upper
cipher = {}

i = 0
while i < len(src):
    cipher[src[i]] = dst[i]
    i = i + 1

s = sys.stdin.read().rstrip()
i = 0
code = ""
while i < len(s):
    if s[i] in cipher:
        code = code + cipher[s[i]]
    else:
        code = code + s[i]
    i = i + 1
sys.stdout.write(code + "\n")

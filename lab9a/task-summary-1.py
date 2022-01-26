#!/usr/bin/env python3

import sys

s = sys.stdin.readlines()
complete = {}

i = 0
while i < len(s):
    curr_file = s[i].rstrip().split(".")
    complete[".".join(curr_file[0:2])] = curr_file[2] == "correct"
    i += 1

for k in complete:
    if complete[k]:
        print(k)

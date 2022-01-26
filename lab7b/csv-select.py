#!/usr/bin/env python3

import sys

args = sys.argv[1]
s = input()
i = 0
#get separate header and value
while args[i] != "=":
    i = i + 1
header = args[:i]
value = args[i + 1:]
#get pos of header
i = 0
pos_head = 0
while s[i:i + len(header)] != header:
    if s[i] == ",":
        pos_head = pos_head + 1
    i = i + 1
#look for value at pos like in last task and check is it equal value
#print and keep going until s = "end"
s = input()
while s != "end":
    j = 0
    pos = 0
    while pos < pos_head:
        if s[j] == ",":
            pos = pos + 1
        j = j + 1
    i = j
    while i < len(s) and s[i] != ",":
        i = i + 1
    if s[j:i] == value:
        print(s)
    s = input()

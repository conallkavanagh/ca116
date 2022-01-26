#!/usr/bin/env python3

import sys
a = sys.argv[1]
b = sys.argv[2]

with open(a) as f:
    a_lines = f.readlines()
with open(b) as f:
    b_lines = f.readlines()

if len(a_lines) < len(b_lines):
    length = len(a_lines)
else:
    length = len(b_lines)

i = 0
while i < length and a_lines[i] == b_lines[i]:
    i = i + 1

char_pos = 0
if i < length:
    a_string = a_lines[i]
    b_string = b_lines[i]
    while a_string[char_pos] == b_string[char_pos]:
        char_pos = char_pos + 1
    print(i, char_pos)
elif len(a_lines) != len(b_lines):
    print(i, char_pos)

#!/usr/bin/env python3

#input = Day Date Month, Year
#           |    |     |
#           a    b     c
#output = Month Date, Year (Day)
s = input()
i = 0
#a, b and c point to the different spaces
a = 0  # first space
b = 0  # second space
c = 0  # ,

while i < len(s):
    if s[i] == ",":
        c = i
        i = i + 1
    elif s[i] == " ":
        if a == 0:
            a = i
        else:
            b = i
    i = i + 1
print(s[b + 1:c] + " " + s[a + 1:b] + ", " + s[c + 2:] + " (" + s[:a] + ")")

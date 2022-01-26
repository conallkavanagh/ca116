#!/usr/bin/env python3

upper = "ABCDEFGHIFKLMNOPQRSTUVWXYZ"
lower = "abcdefghifklmnopqrstuvwxyz"
s = input()

while s != "end":
    i = 0
    new_s = ""
    while i < len(s):
        j = 0
        char = ""
        while j < len(upper):
            if s[i] == upper[j]:
                char = lower[j]
            j = j + 1
        if char == "":
            char = s[i]
        new_s = new_s + char
        i = i + 1
    print(new_s)
    s = input()

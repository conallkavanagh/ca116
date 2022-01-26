#!/usr/bin/env python3

s = input()
i = 0
num = 0

while i < len(s) and num < 2:
    if s[i] >= "0" and s[i] <= "9":
        j = i
        while j < len(s) and s[j] >= "0" and s[j] <= "9":
            j = j + 1
        num = num + 1
        if num == 2:
            print(s[i:j], i)
        i = j
    i = i + 1

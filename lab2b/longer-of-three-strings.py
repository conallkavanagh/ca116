#!/usr/bin/env python3

string1 = input()
string2 = input()
string3 = input()
a = len(string1)
b = len(string2)
c = len(string3)
if a > b and a > c:
    print(string1)
elif b > c:
    print(string2)
else:
    print(string3)

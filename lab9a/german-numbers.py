#!/usr/bin/env python3

import sys

numbers = {
    "one": "eins",
    "two": "zwei",
    "three": "drei",
    "four": "vier",
    "five": "funf",
    "six": "sechs",
    "seven": "sieben",
    "eight": "acht",
    "nine": "neun",
    "ten": "zehn"
}

words = sys.stdin.readlines()
i = 0
while i < len(words):
    print(numbers[words[i].rstrip()])
    i = i + 1

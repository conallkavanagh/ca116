#!/usr/bin/env python3

import sys

s = sys.stdin.readlines()
count = {}
tasks = {}
i = 0
while i < len(s):
    tmp = s[i].split("/")
    user = tmp[0]
    f = tmp[1]
    f_name = ".".join(f.split(".")[0:2])
    if user not in tasks:
        tasks[user] = []
    if f.rstrip().split(".")[2] == "correct":
        j = 0
        while j < len(tasks[user]) and f_name != tasks[user][j]:
            j = j + 1
        if j == len(tasks[user]):
            tasks[user].append(f_name)
    else:
        j = 0
        while j < len(tasks[user]) and f_name != tasks[user][j]:
            j = j + 1
        if j < len(tasks[user]):
            tasks[user].pop(j)
    i += 1
for user in tasks:
    print(user, len(tasks[user]))

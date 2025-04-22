# Problem: Belted Rooms - https://codeforces.com/problemset/problem/1428/B

from collections import defaultdict


t = int(input())
for _ in range(t):

    n = int(input())
    s = input()

    # Count the number of Clockwise and Anti-clockwise belts
    count_clock = count_anti = 0
    for i in range(n):
        if s[i] == '>':
            count_clock += 1
        elif s[i] == '<':
            count_anti += 1
    count = 0
    if count_anti and count_clock:
        for i in range(n):
            if s[i] == '-' or s[(i + 1) % n] == '-':
                count += 1
    else:
        count = n
    
    print(count)
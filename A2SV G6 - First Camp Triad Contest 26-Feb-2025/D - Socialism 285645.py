# Problem: D - Socialism - https://codeforces.com/gym/589822/problem/D

import sys
from collections import Counter
from itertools import accumulate

def input():
    return sys.stdin.readline().strip()

def int_input():
    return int(input())

def list_input():
    return list(map(int, input().split()))

def solve():
    # Your solution logic here
    n, x = map(int, input().split())
    wealth = list_input()

    wealth.sort(reverse= True)
    wealth = list(accumulate(wealth))

    curr = -1
    for i in range(n):
        if wealth[i] / (i + 1) < x:
            curr = i
            break
    
    if curr == -1:
        print(n)
    else:
        print(curr)


def main():
    t = int_input()  # Number of test cases
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
    
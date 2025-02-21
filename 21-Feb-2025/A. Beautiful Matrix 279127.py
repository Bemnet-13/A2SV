# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

import sys

def input():
    return sys.stdin.readline().strip()

def int_map():
    return map(int, input().split())

def int_input():
    return int(input())

def list_input():
    return list(map(int, input().split()))

def solve():
    # Your solution logic here
    
    position = (-1, -1)
    for i in range(5):
        row = list_input()
        if 1 in row:
            c = row.index(1)
            r = i
            position = (r, c)

    
    print(abs(2 - r) + abs(2 - c))

def main():
    t = 1  # Number of test cases
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
    
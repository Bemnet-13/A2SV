# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

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
    n = int_input()
    arr = list_input()

    count = 0

    diff = []
    for i in range(1, n):
        diff.append(arr[i] - arr[i - 1])
    
    seen = set()
    for i in range(len(diff)):

        if diff[i] < 0 and i - 1 not in seen:
            seen.add(i)
            count += 1
    
    print(count)

def main():
    t = int_input()  # Number of test cases
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
    
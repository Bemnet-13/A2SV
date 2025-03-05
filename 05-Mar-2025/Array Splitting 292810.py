# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

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
    n, k = int_map()
    arr = list_input()

    ans = arr[-1] - arr[0]

    diff = []
    for i in range(n - 1):
        diff.append(arr[i] - arr[i + 1])
    
    diff.sort()
    ans += sum(diff[:k - 1])
    print(ans)

def main():
    t = 1  # Number of test cases
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
    
# Problem: I - The Odd Challenge - https://codeforces.com/gym/589822/problem/I

import sys
from itertools import accumulate

def input():
    return sys.stdin.readline().strip()

def int_input():
    return int(input())

def list_input():
    return list(map(int, input().split()))

def solve():
    # Your solution logic here
    n, q = map(int, input().split())
    arr = [0] + list_input()
    ps = list(accumulate(arr))


    for _ in range(q):
        l, r, k = map(int, input().split())
        added = (r - l + 1) * k
        removed = ps[r] - ps[l - 1]
        ans = ps[-1] + added - removed
        if ans % 2 == 1:
            print("YES")
        else:
            print("NO")

def main():
    t = int_input()  # Number of test cases
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
    
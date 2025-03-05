# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

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
    r = list_input()
    m = int_input()
    b = list_input()

    # Prefix sum
    ps_r = [r[0]]
    for i in range(1, n):
        ps_r.append(ps_r[-1] + r[i])
    
    ps_b = [b[0]]
    for i in range(1, m):
        ps_b.append(ps_b[-1] + b[i])
    
    max_b = max(ps_b)
    max_r = max(ps_r)

    ans = max(0, max_b, max_r, max_b + max_r)

    print(ans)       


def main():
    t = int_input()  # Number of test cases
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
    
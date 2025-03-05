# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

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
    n = int_input()
    arr = list_input()
    new_arr = sorted(arr)

    for i in range(1, n):
        arr[i] += arr[i - 1]
        new_arr[i] += new_arr[i - 1]

    q = int_input()

    for _ in range(q):
        type, l, r = int_map()
        r, l = r - 1, l - 1
        # ans = 0
        if type == 1:
            ans = arr[r]
            if l - 1 >= 0:
                ans -= arr[l - 1]
        else:
            ans = new_arr[r]
            if l - 1 >= 0:
                ans -= new_arr[l - 1]
        
        print(ans)

def main():
    t = 1 # Number of test cases
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
    
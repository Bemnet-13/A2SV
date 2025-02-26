# Problem: B - Kidus Couldn't Sleep - https://codeforces.com/gym/589822/problem/B

from itertools import accumulate
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
    n, k = int_map()
    days = list(accumulate(list_input()))
    ans = 0
    for i in range(k - 1, n):
        curr_sum = days[i]
        if i - k >= 0:
            curr_sum -= days[i - k]
         
        ans += curr_sum
    
    res = ans / (n - k + 1)
    print(f"{res:.10f}")

def main():
    t = 1 # Number of test cases
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
    
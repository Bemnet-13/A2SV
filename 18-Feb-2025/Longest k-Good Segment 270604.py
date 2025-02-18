# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

import sys
from collections import Counter

def input():
    return sys.stdin.readline().strip()

def int_input():
    return int(input())

def list_input():
    return list(map(int, input().split()))

def solve():
    # Your solution logic here
    n, k = map(int, input().split())
    a = list_input()
    max_length = 0
    left = 0

    counter = Counter()
    l = 0
    r = -1

    for right in range(n):
        counter[a[right]] += 1
        while left < n and len(counter) > k:
            counter[a[left]] -= 1
            if counter[a[left]] == 0:
                del counter[a[left]]
            
            left += 1
        
        if max_length < right - left + 1:
            max_length = right - left + 1
            l = left + 1
            r = right + 1
    
    print(l, r)
    

def main():
    # t = int_input()  # Number of test cases
    # for _ in range(t):
    solve()

if __name__ == "__main__":
    main()
    
# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

import sys
from collections import deque


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

    ans = n * (n + 1) // 2

    min_ = deque()
    max_ = deque()
    left = 0

    for right in range(n):
        while max_ and max_[-1] > arr[right]:
            max_.pop()
        
        while min_ and min_[-1] < arr[right]:
            min_.pop()
        
        max_.append(arr[right])
        min_.append(arr[right])

        while left < right and abs(max_[0] - min_[0]) > k:
            if arr[left] == max_[0]:
                max_.popleft()
            if arr[left] == min_[0]:
                min_.popleft()

            left += 1
            ans -= (n - right)

    print(ans) 

def main():
    t = 1  # Number of test cases
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
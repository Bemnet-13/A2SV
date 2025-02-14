# Problem: Books - https://codeforces.com/contest/279/problem/B

import sys

def input():
    return sys.stdin.readline().strip()

def int_input():
    return int(input())

def list_input():
    return list(map(int, input().split()))

def solve():
    # Your solution logic here
    n, k = map(int, input().split())
    minutes = list_input()
    minutes = minutes

    curr_minutes = 0
    left = 0
    max_books = 0

    for right in range(len(minutes)):
        while curr_minutes + minutes[right] > k:
            curr_minutes -= minutes[left]
            left += 1
        
        curr_minutes += minutes[right]
        max_books = max(max_books, right - left + 1)
        
    return max_books

def main():

    ans = solve()
    print(ans)

if __name__ == "__main__":
    main()
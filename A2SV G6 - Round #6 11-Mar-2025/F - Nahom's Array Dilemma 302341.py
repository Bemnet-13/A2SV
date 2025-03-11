# Problem: F - Nahom's Array Dilemma - https://codeforces.com/gym/594077/problem/F

import sys

def input():
    return sys.stdin.readline().strip()

def int_map():
    return map(int, input().split())

def int_input():
    return int(input())

def list_input():
    return list(map(int, input().split()))

def prev_greater(n, arr):
    ps = [0, arr[0]]
    for i in range(1, len(arr)):
        ps.append(ps[-1] + arr[i])
    
    # Find the previous greater element
    
    stack = []
    for i in range(n):
        idx = 0
        while stack and arr[stack[-1]] <= arr[i]:
            idx = stack.pop()
            if ps[i] - ps[idx] > 0:
                return False

        stack.append(i)
    
    return True

def solve():
    # Your solution logic here
    n = int_input()
    arr = list_input()

    return prev_greater(n, arr) and prev_greater(n, arr[::-1])

def main():
    t = int_input()  # Number of test cases
    for _ in range(t):
        ans = solve()
        if ans:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
    
# Problem: Skibidus and Fanum Tax (hard version) - http://codeforces.com/problemset/problem/2065/C2

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
    n, m = int_map()
    a = list_input()
    b = list_input()

    b.sort()

    def feasible(curr, prev):
        left = 0
        right = m - 1
        ans = float('inf')

        while left <= right:
            mid = (left + right) // 2

            change = b[mid] - curr
            if change >= prev:
                ans = change
                right = mid - 1
            else:
                left = mid + 1
        
        return ans

    
    prev = float('-inf')
    for i in range(n):
        min_change = feasible(a[i], prev)
        if min_change == float('inf') and a[i] < prev:
            return False

        if min_change != float('inf') and a[i] < prev and min_change < prev:
            return False
        
        if min(a[i], min_change) >= prev:
            a[i] = min(a[i], min_change)
        else:
            a[i] = min_change
        prev = a[i]
    
    return True


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
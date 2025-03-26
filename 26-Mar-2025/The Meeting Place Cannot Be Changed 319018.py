# Problem: The Meeting Place Cannot Be Changed - https://codeforces.com/problemset/problem/780/B

import sys

def input():
    return sys.stdin.readline().strip()

def int_map():
    return map(int, input().split())

def int_input():
    return int(input())

def list_input():
    return list(map(int, input().split()))


def good(pos, speed, mid):
    time_left = 0
    time_right = 0
    first = mid + 0.0000001
    second = mid - 0.0000001
    
    for i in range(len(pos)):
        time_left = max(abs(first - pos[i]) / speed[i], time_left)
        time_right = max(abs(second - pos[i]) / speed[i], time_right)
    
    return time_left,  time_right


def solve():
    # Your solution logic here
    
    n = int_input()
    pos = list_input()
    speed = list_input()

    low = 0
    high = max(pos)

    ans = float('inf')

    for _ in range(60):
        mid = (low + high) / 2

        time_left, time_right = good(pos, speed, mid)

        if time_left < time_right:
            low = mid + 0.0000001
        else:
            high = mid - 0.0000001
            
        ans = min(time_left, time_right)
    
    print(ans)

def main():
    t = 1 # Number of test cases
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
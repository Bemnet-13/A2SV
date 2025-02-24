# Problem: Fox And Snake - https://codeforces.com/problemset/problem/510/A

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
    ans = []
    end = True
    for i in range(n):
        if i % 2 == 0:
            ans.append("#"*m)
        else:
            if end:
                ans.append("."*(m - 1) + "#")
                end = not end
            else:
                ans.append("#" + "."*(m - 1) )
                end = not end
    
    for line in range(len(ans)):
        print(ans[line])
def main():
    t = 1  # Number of test cases
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
    
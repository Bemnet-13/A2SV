# Problem: E - Minimum Subsequence - https://codeforces.com/gym/594077/problem/E

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
    num = input()


    count = 0
    zeros = []
    ones = []
    ans = [1] * n

    for i in range(n):
        if num[i] == '1':
            if zeros:
                c = zeros.pop()
            else:
                count += 1
                c = count
            ans[i] = c
            ones.append(c)
        else:
            if ones:
                d = ones.pop()
            else:
                count += 1
                d = count
            ans[i] = d
            zeros.append(d)

    print(len(ones) + len(zeros))
    print(*ans)

        

def main():
    t = int_input()  # Number of test cases
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
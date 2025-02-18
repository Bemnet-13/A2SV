# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

import sys

def input():
    return sys.stdin.readline().strip()

def int_input():
    return int(input())

def list_input():
    return list(map(int, input().split()))

def solve():
    # Your solution logic here
    n, k, q = map(int, input().split())
    recipes = []
    queries = []
    for _ in range(n):
        recipe = list_input()
        recipes.append(recipe)
    
    temps = [0] * 200001

    for l, r in recipes:
        temps[l] += 1
        if r + 1 < len(temps):
            temps[r + 1] -= 1
    
    for i in range(1, len(temps)):
        temps[i] += temps[i - 1]
    
    for i in range(1, len(temps)):
        temps[i] = 0 if temps[i] < k else 1

    for i in range(1, len(temps)):
        temps[i] += temps[i - 1]

    ans = []
    for _ in range(q):
        l, r = map(int, input().split())
        if l - 1 < len(temps):
            print(temps[r] - temps[l - 1])
        else:
            print(temps[r])

    
    print(*ans, sep='\n')


def main():
    # t = int_input()  # Number of test cases
    # for _ in range(t):
    solve()

if __name__ == "__main__":
    main()
    
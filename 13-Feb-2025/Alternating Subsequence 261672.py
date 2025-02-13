# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    curr_max = a[0]
    max_sum = 0

    for right in range(1, n):
        if a[right] * a[right - 1] > 0:
            curr_max = max(curr_max, a[right])
        else:
            max_sum += curr_max
            curr_max = a[right]



    print(max_sum + curr_max)
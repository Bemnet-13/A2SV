# Problem: Number of smaller - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.append(float('inf'))

i = 0
j = 0
ans = []

while i < n + 1 and j < m:
    if b[j] > a[i]:
        i += 1
    else:
        ans.append(i)
        j += 1

print(*ans) 
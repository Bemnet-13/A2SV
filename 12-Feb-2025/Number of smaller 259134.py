# Problem: Number of smaller - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B

n, m = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

ans = []
j = 0

for i in range(m):

    while j< n and arr2[i] > arr1[j]:
        j += 1
    ans.append(j)

print(*ans)
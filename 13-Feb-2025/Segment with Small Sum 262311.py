# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

n, s = map(int, input().split())

arr = list(map(int, input().split()))

ans = 0
left = 0
curr_sum = 0

for right in range(n):
    curr_sum += arr[right]
    while left < n and curr_sum > s:
        curr_sum -= arr[left]
        left += 1
    
    ans = max(ans, right - left + 1)

print(ans)
# Problem: Limited Repainting - https://codeforces.com/contest/2070/problem/C

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    penalty = list(map(int, input().split()))

    def good(max_pen):
        flips = 0
        is_painting = False
        for i in range(n):
            if penalty[i] > max_pen:
                if s[i] == "R":
                    is_painting = False
                else:
                    if not is_painting:
                        is_painting = True
                        flips += 1
        
        return flips <= k


    # Binary search
    left, right = 0, max(penalty)
    ans = right

    while left <= right:
        mid = (left + right) // 2
        if good(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    
    print(ans)
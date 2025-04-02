# Problem: Masha and a Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    ans = 0
    canBeSwapped = True
    def min_swaps(left, right):
        global ans
        global canBeSwapped
        if left == right:
            return arr[left], arr[right]

        mid = (left + right) // 2
        left_min, left_max = min_swaps(left, mid)
        right_min, right_max = min_swaps(mid + 1, right)
        
        if left_max > right_min and left_min - right_max == 1:
            ans += 1
        elif left_max > right_min:
            canBeSwapped = False
        
        return min(left_min, right_min), max(left_max, right_max)
    
    min_swaps(0, n - 1)
    if canBeSwapped:
        print(ans)
    else:
        print(-1)
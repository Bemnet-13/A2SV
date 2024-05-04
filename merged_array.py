n , m = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

merged = [0] * (n + m)

p1 = p2 = 0
p3 = 0

while p1 + p2 < n + m:
    if p1 < n and p2 < m:
        if arr1[p1] < arr2[p2]:
            merged[p3] = arr1[p1]
            p1 += 1
        else:
            merged[p3] = arr2[p2]
            p2 += 1
    else:
        if p1 >= n:
            merged[p3] = arr2[p2]
            p2 += 1
        else:
            merged[p3] = arr1[p1]
            p1 += 1
    
    p3 += 1

merged = [str(n) for n in merged]
print(' '.join(merged))

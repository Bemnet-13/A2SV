n , m = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

p2 = p1 = 0
smaller = []

while p2 < m:
    if arr1[p1] < arr2[p2]:
        if p1 == n - 1:
            smaller.append(p1 + 1)
            p2 += 1
            continue
        p1 += 1
    else:
        smaller.append(p1)
        p2 += 1
    

smaller = [str(n) for n in smaller]
print(' '.join(smaller))


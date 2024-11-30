n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))


i = j = 0
ans = []

while i < n and j < m:
    if arr1[i] < arr2[j]:
        ans.append(arr1[i])
        i += 1
    else:
        ans.append(arr2[j])
        j += 1

if i < n:
    ans.extend(arr1[i:])
if j < m:
    ans.extend(arr2[j:])

ans = [str(i) for i in ans]

res = " ".join(ans)


print(res)



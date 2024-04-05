from collections import defaultdict
n, m = map(int, input().split())

a = defaultdict(list)
b = []


for i in range(n):
    chr = input()
    a[chr].append(i + 1)

for i in range(m):
    chr = input()
    b.append(chr)

for i in b:
    if i not in a:
        print(-1)
    else:
        lst = a[i]
        for j in lst:
            print(j, end = " ")
        print()
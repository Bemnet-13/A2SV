arr = []

for _ in range(5):
    arr.append(int(input()))

print("Enter the number to be searched")
n = int(input())

count = 0
found = False
for num in arr:
    if num == n:
        found = True
        count += 1
print(count)
if not found:
    print(-1)
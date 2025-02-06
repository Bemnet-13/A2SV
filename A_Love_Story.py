t = int(input())

for _ in range(t):
    s = input()
    STRING = 'codeforces'

    count = 0
    for i in range(10):
        if STRING[i] != s[i]:
            count += 1
    
    print(count)
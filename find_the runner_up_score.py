if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    for k in range(len(arr)-1, -1, -1):
        if arr[k] != arr[-1]:
            print(arr[k])
            break    
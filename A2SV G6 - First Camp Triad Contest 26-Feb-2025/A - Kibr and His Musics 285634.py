# Problem: A - Kibr and His Musics - https://codeforces.com/gym/589822/problem/A

import sys

def input():
    return sys.stdin.readline().strip()

def int_map():
    return map(int, input().split())

def int_input():
    return int(input())

def list_input():
    return list(map(int, input().split()))

def solve():
    # Your solution logic here
    n, m  = int_map()
    playlist = []

    for _ in range(n):
        c, t = int_map()
        playlist.append(t * c)
    
    for i in range(1, len(playlist)):
        playlist[i] += playlist[i - 1]
    
    arr = list_input()
    for min_ in arr:
        left , right = 0, n - 1
        found = False
        while left < right:
            mid = (left + right) // 2
            if playlist[mid] == min_:
                left = mid
                break
            elif playlist[mid] < min_:
                left = mid + 1
            else:
                right = mid
           
        print(left + 1)



def main():
    t = 1 # Number of test cases
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
    
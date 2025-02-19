# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F

import sys
from collections import Counter

def input():
    return sys.stdin.readline().strip()

def int_input():
    return int(input())

def list_input():
    return list(map(int, input().split()))

def solve():
    k = int_input()
    s = input()

    ans = at_most(s, k)
    if k != 0:
        ans -= at_most(s, k - 1)
    print(ans)
    


def at_most(s, k):
    counter = Counter()
    left = 0
    subarrays = 0

    for right in range(len(s)):
        counter[s[right]] += 1

        while left < len(s) and counter['1'] > k:
            counter[s[left]] -= 1
            if counter[s[left]] == 0:
                del counter[s[left]]
            left += 1

        subarrays += right - left + 1
    
    return subarrays

def main():
    solve()

if __name__ == "__main__":
    main()
# Problem: D - Creating an a-Good String - https://codeforces.com/gym/596141/problem/D

import sys
import threading

input_fn = lambda: sys.stdin.readline().strip()

def main():

    def solve():
       n = int(input())
       s = input()
       ans = recursive(s, ord('a'), 0, n - 1)
       print(ans)

    def recursive(s, letter_pos, start, end):
        if end == start:
            if s[end] != chr(letter_pos):
                return 1
            
            return 0
        

        mid = (start + end) // 2
        left_score = 0
        right_score = 0

        for i in range(start, mid + 1):
            if s[i] != chr(letter_pos):
                left_score += 1
        
        for j in range(mid + 1, end + 1):
            if s[j] != chr(letter_pos):
                right_score += 1
        
        next_letter = letter_pos + 1

        ans1 = left_score + recursive(s, next_letter, mid + 1, end)
        ans2 = right_score + recursive(s, next_letter, start, mid)

        return min(ans1, ans2)

            



    t = int(input())
    for _ in range(t):
        solve()



if __name__ == '__main__':
    # sys.setrecursionlimit(1 << 30)
    # threading.stack_size(1 << 27)
    # main_thread = threading.Thread(target=main)
    # main_thread.join()
    # main_thread.start()

    main()






# def solve(s, c = 'a'):
#     n = len(s)
#     if n == 1:
#         return 0 if s == c else 1
    
#     mid = n // 2
#     next = chr(ord(c) + 1)
    
#     left = sum(1 for i in range(mid) if s[i] != c)
#     right = solve(s[mid:], next)

    
#     other_right = sum(1 for i in range(mid, n) if s[i] != c)
#     other_left = solve(s[:mid], next)
    
#     return min(left + right, other_left + other_right)


# t = int(input())

# for _ in range(t):
#     n = int(input())
#     s = input()
#     print(solve(s))
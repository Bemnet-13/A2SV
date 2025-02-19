# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr = [0] * len(s)
        for start, end, dir_ in shifts:
            x, y = 1, -1
            if dir_ == 0: x, y = -1, 1 # Change the direction
            arr[start] += x
            if end + 1 < len(arr): arr[end + 1] += y

        ps = list(accumulate(arr))
        ans = []
        for index, letter in enumerate(s):
            sg = ord(letter) - ord('a')
            sg = (sg + ps[index]) % 26 + ord('a')
            ans.append(chr(sg))
        
        return "".join(ans)
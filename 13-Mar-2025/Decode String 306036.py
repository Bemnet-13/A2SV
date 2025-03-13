# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        mult = []
        letter = []
        curr_ext = ""

        for i in range(len(s)):
            if s[i] == "[":
                mult[-1][0] = int(mult[-1][0]) 

            elif s[i].isdigit():
                if not mult or mult and isinstance(mult[-1][0], int):
                    mult.append([s[i], i])
                else:
                    mult[-1][0] += s[i]
                
                if curr_ext != "":
                    letter.append([curr_ext, i - 1])
                    curr_ext = ""

            elif s[i].isalpha():
                curr_ext += s[i]

            else:
                if curr_ext != "":
                    letter.append([curr_ext, i])
                    curr_ext = ""
                
                c, sub = mult.pop(), letter.pop()
                curr, j = c
                top, index = sub

                while letter and j < letter[-1][1]:
                    letter[-1][0] += top
                    top, index = letter.pop()

                crnt = top * curr
                letter.append([crnt, index])

        ans = ""
        for i in range(len(letter)):
            ans += letter[i][0]

        return ans + curr_ext
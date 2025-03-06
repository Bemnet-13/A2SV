# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.stackBuilder(s) == self.stackBuilder(t)
    
    def stackBuilder(self, string):
        stack = []
        for letter in string:
            if letter == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(letter)

        return stack
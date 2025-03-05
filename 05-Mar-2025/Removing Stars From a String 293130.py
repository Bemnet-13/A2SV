# Problem: Removing Stars From a String - https://leetcode.com/problems/removing-stars-from-a-string/

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for letter in s:
            if letter != "*":
                stack.append(letter)
            else:
                if stack:
                    stack.pop()
            

        return "".join(stack)
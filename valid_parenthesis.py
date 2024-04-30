class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {'(':')', '{':'}', '[' : ']'}
        stack = []

        for chr in s:
            if len(stack) == 0:
                stack.append(chr)
            elif chr not in dictionary and dictionary.get(stack[-1]) == chr:
                stack.pop()
            else:
                stack.append(chr)
            
        
        if len(stack) == 0:
            return True
        return False
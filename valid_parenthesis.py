class Solution:
    def isValid(self, s):
        stack = []
        dictionary = {'(':')', '{':'}', '[':']'}

        for i in s:
            if i in s.keys():
                stack.append(i)

            else:
                if not stack:
                    return False
                else:
                    val = stack.pop()
                    if i != dictionary[val]:
                        return False
        
        return stack == []
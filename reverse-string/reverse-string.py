class Solution:
    def reverseString(self, s) -> None:
        self.printReverse(0, s)
        
        """
        Do not return anything, modify s in-place instead.
        """
    def printReverse(self, index, s):
        if index >= len(s) // 2:
            return
        s[index], s[len(s) - 1 - index] = s[len(s) - 1 - index], s[index]
        self.printReverse(index + 1, s)
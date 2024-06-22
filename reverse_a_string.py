class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        def reverseMachine(i, s):
            if i == len(s) // 2:
                return
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
            print(i)
            print(s)
            reverseMachine(i + 1, s)
        
        reverseMachine(i , s)


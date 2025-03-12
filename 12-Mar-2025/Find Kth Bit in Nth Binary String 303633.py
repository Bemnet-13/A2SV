# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def reverseInvert(ans):
            for i in range(len(ans)):
                if ans[i] == "0":
                    ans[i] = "1"
                else:
                    ans[i] = "0"
            return ans[::-1]

        def buildStr(n):
            if n == 1:
                return ["0"]
            ans = buildStr(n - 1)
            return ans + ["1"] + reverseInvert(ans)

        string = buildStr(n)
        return string[k - 1]
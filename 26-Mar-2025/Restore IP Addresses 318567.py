# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        def validNumber(s):
            if int(s) > 255 or (s[0] == '0' and len(s) >= 2):
                return False
            
            return True

        def backtrack(path, index, part):
            nonlocal ans
            if len(path) == 4:
                if validNumber(path[-1]) and index == len(s):
                    ans.append(".".join(path))
                return
            
            curr = []
            for i in range(index, len(s)):
                curr.append(s[i])
                num = "".join(curr)
                if validNumber(num):
                    path.append(num)
                    backtrack(path, i + 1, part + 1)
                    path.pop()
        
        backtrack([], 0, 0)
        return ans
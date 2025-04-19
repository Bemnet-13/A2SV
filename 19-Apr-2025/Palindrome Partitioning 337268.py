# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrome(string):
            l, r = 0, len(string) - 1
            while l < r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            return True

        def validPartition(strings):
            for string in strings:
                if not isPalindrome(string):
                    return False
            return True
        
        n = len(s)
        ans = []
        def backtrack(i, path):
            # If at the end of the string 
            nonlocal ans
            if i >= n:
                if validPartition(path):
                    ans.append(deepcopy(path))
                return
            
            if path and not isPalindrome(path[-1]):
                return

            for next_index in range(i + 1, n + 1):            
                substring = s[i:next_index]
                path.append(substring)
                backtrack(next_index, path)
                path.pop()

        backtrack(0, [])
        return ans 
                
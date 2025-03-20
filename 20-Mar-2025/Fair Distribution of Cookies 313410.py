# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        max_ = sum(cookies)

        def backtrack(path, index):
            nonlocal max_
            if index == len(cookies):
                mx = max(path)
                max_ = min(mx, max_)              
                return
            
            for i in range(len(path)):
                path[i] += cookies[index]
                backtrack(path, index + 1)
                path[i] -= cookies[index]
        

        if len(cookies) == k:
            return max(cookies)
        p = [0] * k
        backtrack(p, 0)
        return max_
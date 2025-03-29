# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        def good(capacity):
            children = 0
            for subpile in candies:
                children += subpile // capacity
            
            return children >= k      

        left = 1
        right = max(candies)
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if good(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans
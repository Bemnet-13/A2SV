# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        ans = 0
        left, right, n = 0, len(citations) - 1, len(citations)

        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if citations[mid] <= n - mid:    
                left = mid + 1
            else:
                right = mid - 1

            ans = max(ans, min(citations[mid], n - mid))
        
        return ans
# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def valid(k):
            hours = 0

            for i in piles:
                hours += ceil(i / k)
            
            return hours <= h
        
        low = 1
        high = sum(piles)

        while low <= high:
            mid = (low + high) // 2
            if valid(mid):
                high = mid - 1
            else:
                low = mid + 1
        
        return low
# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def validate(capacity):
            d = 1
            c = 0
            for i in range(len(weights)):
                c += weights[i]
                if c > capacity:
                    d += 1
                    c = weights[i]
            
            return d <= days
        
        low = max(weights)
        high = sum(weights)

        while low <= high:
            mid = (low + high) // 2
            if validate(mid):
                high = mid - 1
            else:
                low = mid + 1
        
        return low

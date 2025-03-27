# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        def good(minutes):
            
            c = cars
            for i in range(len(ranks)):
                cars_repaired = floor(sqrt(minutes / ranks[i]))
                c -= cars_repaired

            return c <= 0
        
        low = 0
        high = max(ranks) * cars * cars
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if good(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
            
        return ans
# Problem: Heaters - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def good(radius):
            heater_pos = 0
            for pos in range(len(houses)):
                while heater_pos < len(heaters) and abs(houses[pos] - heaters[heater_pos]) > radius:
                    heater_pos += 1
                if heater_pos >= len(heaters):
                    return False
            
            return True
        

        left, right = 0, max(houses[-1], heaters[-1])
        ans = right

        while left <= right:
            mid = (left + right) // 2
            if good(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
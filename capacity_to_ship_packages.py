class Solution:
    def shipWithinDays(self, weights, days) -> int:
        def capacityChecker(capacity):
            currentCapacity = capacity
            ships = 1
            for w in weights:
                if w > currentCapacity:
                    ships += 1
                    currentCapacity = capacity
                currentCapacity -= w
            return ships <= days
        left , right = max(weights), sum(weights)

        while left < right:
            
            mid = (left + right) // 2
            if capacityChecker(mid):
                right = mid
            else:
                left = mid + 1
        return left
    
trial = Solution()
o = trial.shipWithinDays(weights = [3,2,2,4,1,4], days = 3)
print(o)
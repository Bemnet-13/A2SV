class Solution:
    def minEatingSpeed(self, piles, h) -> int:
        left, right = min(piles), max(piles)

        # Binary search
        def finishedBeforeGuardsComing(speed):
            total_time = 0

            for i in piles:
                
                t = (i // speed)
                if i % speed != 0:
                    t += 1
                total_time += t
            return total_time <= h

        while left < right:
            mid = (left + right) // 2
            if finishedBeforeGuardsComing(mid):
                right = mid
            else:
                left = mid + 1
       
        return left
    
trial = Solution()
o = trial.minEatingSpeed(piles = [30,11,23,4,20], h = 6)
print(o)
        
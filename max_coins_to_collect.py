class Solution:
    def maxCoins(self, piles) -> int:
        n = len(piles) // 3
        
        i = 1
        count = 0
        while n > 0:
            count += piles[i]
            n -= 1
            i += 1
        return count
# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)

        ans = 0
        curr = 1
        iters = 0
        while iters < len(piles) // 3:
            ans += piles[curr]
            curr += 2
            iters += 1

        return ans 
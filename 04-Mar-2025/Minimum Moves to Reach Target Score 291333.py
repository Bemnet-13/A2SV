# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0

        while target > 1:
            if target % 2 == 0 and maxDoubles > 0:
                target //= 2
                maxDoubles -= 1
            elif maxDoubles > 0:
                target -= 1
            else:
                ans += (target - 1)
                break
            ans += 1
        return ans
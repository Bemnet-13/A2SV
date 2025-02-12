# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_ = max(costs)

        freq = [0] * (max_ + 1)
        # Counting the frequencies
        for cost in costs:
            freq[cost] += 1

        ans = 0
        min_ = min(costs)

        for i in range(min_, max_ + 1):
            k = freq[i]
            while k > 0:
                if coins - i >= 0:
                    ans += 1
                    coins -= i
                else:  
                    break
                k -= 1
        
        return ans
from collections import defaultdict
class Solution:
    def maxIceCream(self, costs, coins) -> int:
        counter = defaultdict(int)

        for cost in costs:
            counter[cost] += 1
        
        max_cost = max(costs)
        min_cost = min(costs)

        total = 0
        for i in range(min_cost, max_cost + 1):
            val = counter.get(i)
            if val != None and coins >= i:
                while val > 0:
                    if coins < i:
                        return total
                    coins -= i
                    total += 1
                    val -= 1
                
        return total

# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x : x[1] - x[0])
        ans = 0
        n = len(costs) // 2
        
        for i, interval in enumerate(costs):
            a, b = interval
            if i < n:
                ans += b
            else:
                ans += a
        
        return ans
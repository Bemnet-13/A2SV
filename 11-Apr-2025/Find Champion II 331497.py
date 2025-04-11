# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        losers = set()
        winners = set()
        for u, v in edges:
            losers.add(v)
            winners.add(u)
        
        in_connection = losers | winners
        for i in range(n):
            if i not in in_connection:
                winners.add(i)
        
        non_losers = winners - losers
        if len(non_losers) != 1: return -1
        return non_losers.pop()
            
# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        curr = [1]
        for i in range(rowIndex):
            curr = self.pascalCalc(curr, [1])
        
        return curr
    
    def pascalCalc(self, prev, curr):
        if len(curr) == len(prev):
            curr.append(1)
            return curr
            
        last = len(curr)
        curr.append(prev[last] + prev[last - 1])
        return self.pascalCalc(prev, curr)
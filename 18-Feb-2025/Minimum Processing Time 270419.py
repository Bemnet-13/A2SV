# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse = True)
        tasks.sort()
        
        max_ = 0
        for i in range(len(processorTime)):
            max_ = max(max_, processorTime[i] + tasks[i * 4 + 3])
        
        return max_
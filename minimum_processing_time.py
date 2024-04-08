class Solution:
    def minProcessingTime(self, processorTime, tasks) -> int:
        processorTime.sort(reverse = True)
        tasks.sort()
        time_consumed = []

        for i in range(len(processorTime)):
            time_consumed.append(processorTime[i] + tasks[(i + 1)* 4 -1])
        
        return max(time_consumed)
    
trial = Solution()
o = trial.minProcessingTime(processorTime = [10,20], tasks = [2,3,1,2,5,8,4,3])
print(o)
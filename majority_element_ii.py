class Solution:
    def majorityElement(self, nums):
        candidates = [[0,0], [0,0]]
        treshold = len(nums) // 3
        
        for num in nums:
            found = False
            for i in range(2):
                if candidates[i][0] == num:
                    candidates[i][1] += 1
                    found = True
                    break
            
            if not found:
                for i in range(2):
                    if candidates[i][1] == 0:
                        candidates[i] = [num, 1]
                        found = True
                        break
            if not found:
                for i in range(2):
                    candidates[i][1] -= 1
        
        ans = []
        for c in candidates:
            c_count = nums.count(c[0])
            if c_count > treshold:
                ans.append(c[0])
        
        return ans
    
trial = Solution()
print(trial.majorityElement([2,2,1,3]))
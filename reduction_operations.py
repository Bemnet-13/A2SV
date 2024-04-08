class Solution:
    def reductionOperations(self, nums) -> int:
        nums.sort()

        l, r = len(nums)-2, len(nums)-1
        
        min_ops = 0
        while l >= 0:
            if nums[r] == nums[0]:
                break
            if nums[l] != nums[r]:
                min_ops += len(nums) - r    
            l -= 1
            r -= 1

        return min_ops
            
trial = Solution()
o = trial.reductionOperations(nums = [1,1,2,2,3])
print(o)

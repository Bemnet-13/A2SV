class Solution:
    def productExceptSelf(self, nums):
        nums_forward = [nums[0]]
        for i in range(1, len(nums)):
            nums_forward.append(nums_forward[-1] * nums[i])
       
        nums_backward = [nums[-1]]
        for i in range(len(nums) - 2, -1, -1):
            nums_backward.insert(0, nums_backward[0] * nums[i])
        
        ans = [0] * len(nums)
        i = 0
        while i < len(nums):
            if i == 0:
                ans[i] = nums_backward[i + 1]
            elif i ==  len(nums) - 1:
                ans[i] = nums_forward[i - 1]
            else:
                ans[i] = nums_forward[i - 1] * nums_backward[i + 1]
            i += 1
        return ans
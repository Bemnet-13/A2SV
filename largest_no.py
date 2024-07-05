class Solution:
    def largestNumber(self, nums) -> str:
        # 997
        # 9
        nums = [str(i) for i in nums]
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if self.greater(nums[j], nums[i]):
                    nums[i], nums[j] = nums[j], nums[i]
        
        print(nums)
                    

    def greater(self, num1, num2):
        # length = min(len(num1), len(num2))

        res1 = num1 + num2
        res2 = num2 + num1
        if res1 >= res2:
            return True
        else:
            return False

# trial = Solution()
# trial.largestNumber(nums = [93,30,34,5,9])
# 
# [9, 30, 34, 5,3]
# [9, ]
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        product_with_out_zeros = 1
        zeros_count = 0
        for num in nums:
            if num == 0:
                zeros_count += 1
            else:
                product_with_out_zeros *= num
        
        product = 0 if zeros_count != 0 else product_with_out_zeros

        for i in range(n):
            if nums[i] != 0:
                nums[i] = product_with_out_zeros // nums[i]
            elif nums[i] == 0 and zeros_count > 1:
                nums[i] = 0
            else:
                nums[i] = product_with_out_zeros
        
        return nums
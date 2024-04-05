class Solution:
    def applyOperations(self, nums):
        new_nums = []
        count_0 = 0
        for i in range(len(nums-1)):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i + 1] = 0
            if nums[i] != 0:
                new_nums.append()
            else:
                count_0 += 1
        
        if nums[-1] == 0:
            count_0 += 1
        else:
            new_nums.append(nums[-1])
        return new_nums + ([0] * count_0)
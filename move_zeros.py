class Solution:
    def moveZeroes(self, nums) -> None:
        l, r = 0, 1

        while r < len(nums):
            if nums[l] == 0 and nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r += 1
            elif nums[r] == 0 and nums[l] == 0:
                r += 1
            else:
                l += 1
                r += 1


trial =Solution()
trial.moveZeroes([1,0,0,0,0,0,0,1,2])
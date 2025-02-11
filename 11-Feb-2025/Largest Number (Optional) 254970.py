# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] + nums[i] >nums[i] + nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

        return str(int("".join(nums)))     
# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = set()
        i = 0
        
        while i < len(nums):
            corr_pos = nums[i] - 1
            if nums[i] == nums[corr_pos] and i != corr_pos:
                ans.add(nums[i])
                i += 1
            elif nums[i] != nums[corr_pos]:
                nums[corr_pos], nums[i] = nums[i], nums[corr_pos]
            else:
                i += 1

        return list(ans)
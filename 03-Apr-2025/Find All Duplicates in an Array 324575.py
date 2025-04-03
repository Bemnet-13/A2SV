# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = set()

        i = 0
        while i < len(nums):
            val = nums[i]
            if val == i + 1:
                i += 1
            else:
                if nums[i] == nums[val - 1]:
                    ans.add(val)
                    i += 1
                    continue
                nums[i], nums[val - 1] = nums[val - 1], nums[i]
        
        return list(ans)
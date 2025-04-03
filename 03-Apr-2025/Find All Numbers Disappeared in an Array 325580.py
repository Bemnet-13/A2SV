# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = set()
        i = 0
        
        while i < len(nums):
            corr_pos = nums[i] - 1
            if nums[i] == nums[corr_pos] and i != corr_pos:
                ans.add(i + 1)
                i += 1
            elif nums[i] != nums[corr_pos]:
                if nums[i] in ans:
                    ans.remove(nums[i])
                nums[corr_pos], nums[i] = nums[i], nums[corr_pos]  
            else:
                i += 1

        return list(ans)
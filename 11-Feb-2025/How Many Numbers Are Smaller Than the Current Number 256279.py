# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new_nums = [(ind, num) for ind, num in enumerate(nums)]
        new_nums.sort(key = lambda pair: pair[1])

        ans = [0] * len(nums)
        for i in range(len(new_nums)):
            curr_ind, curr_num = new_nums[i]
            if curr_num == new_nums[i - 1][1]:
                ans[curr_ind] = ans[new_nums[i - 1][0]]
                
            else:
                ans[curr_ind] = i

        
        return ans
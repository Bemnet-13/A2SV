# Problem: 3Sum - https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        seen = {}

        for i in range(n - 2):
            target = -nums[i]
            l = i + 1
            r = n - 1
            while l < r:
                curr_sum = nums[l] + nums[r]
                if curr_sum > target:
                    r -= 1
                elif curr_sum < target:
                    l += 1
                else:
                    if (nums[i], nums[l]) not in seen:
                        ans.append([nums[i], nums[l], nums[r]])
                        seen[(nums[i], nums[l])] = nums[r]
                    l += 1
                    r -= 1
        return ans

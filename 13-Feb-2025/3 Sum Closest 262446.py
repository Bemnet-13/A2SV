# Problem: 3 Sum Closest - https://leetcode.com/problems/3sum-closest/description/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff = math.inf
        n = len(nums)

        sum_closest = -1
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if abs(three_sum - target) < min_diff:
                    min_diff = abs(three_sum - target)
                    sum_closest = three_sum

                if target == three_sum:
                    return sum_closest
                elif target > three_sum:
                    left += 1
                else:
                    right -= 1
            
        
        return sum_closest

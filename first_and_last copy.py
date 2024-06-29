class Solution:
    def searchRange(self, nums, target: int):
        low_l = 0
        low_r = len(nums) - 1
        
        lower_idx = len(nums)
        while low_l < low_r:
            mid = low_l + (low_r - low_l) // 2
            if nums[mid] == target:
                low_r = mid + 1
                lower_idx = min(lower_idx, mid)
            elif nums[mid] < target:
                low_l = mid
            else:
                low_r = mid
        print(lower_idx)
            
trial = Solution()
trial.searchRange(nums = [5,7,7,8,8,10], target = 8)

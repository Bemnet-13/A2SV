class Solution:
    def findMin(self, nums) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[l] < nums[mid]:
                r = mid
            else:
                break
        return nums[l]
trial = Solution()
o = trial.findMin(nums = [11,13,15,17])
print(o)
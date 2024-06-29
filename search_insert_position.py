class Solution:
    def searchInsert(self, nums, target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        if l == len(nums) - 1 and nums[l] != target:
            return l + 1
        return l
    
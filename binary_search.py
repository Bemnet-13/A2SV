class Solution:
    def search(self, nums, target) -> int:
        def binary_search(l, r, nums, target):
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binary_search(l, mid, nums, target)
            elif nums[mid] < target:
                return binary_search(mid + 1, r, nums, target)
            else:
                return -1
        return binary_search(0, len(nums) - 1,nums, target)
    
trial = Solution()
o = trial.search(nums = [-1,0,3,5,9,12], target = 11)
print(o)
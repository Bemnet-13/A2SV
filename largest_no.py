class Solution:
    def largestNumber(self, nums) -> str:
        nums.sort(key = self.sorter, reverse = True)
        print(nums)

    def sorter(self, item):   
        return int(str(item)[0])

trial = Solution()
trial.largestNumber(nums = [3,30,34,5,9])
import math
class Solution:
    def subarrayGCD(self, nums, k: int) -> int:
        count = 0

        start = end = 0

        while start < len(nums) and end < len(nums):
            if nums[start] % k != 0:
                start += 1
                end = start
            elif nums[start] % k == 0:
                true_gcd = self.gcd_calculator(start, end, nums)
                if true_gcd == k:
                    print(nums[start], nums[end])
                    count += 1
                    if end < len(nums) - 1:
                        end += 1
                    elif end == len(nums) - 1:
                        start += 1
                        end = start
                elif nums[end] % k != 0:
                    start += 1
                    end = start
                else:
                    end += 1
        return count
    def gcd_calculator(self, start, end, nums):
        cal = math.inf
        for i in range(start, end + 1):
            for j in range(i, end + 1):
                cal = min(self.gcd(nums[i], nums[j]), cal)
        return cal

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

trial = Solution()
o = trial.subarrayGCD([3,12,9,6], 3)
print(o)
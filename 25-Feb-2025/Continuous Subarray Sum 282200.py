# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        count = defaultdict(list)
        count[0].append(-1)
        sum_ = 0
        subarrays = 0
        
        for index, num in enumerate(nums):
            sum_ += num
            rem = sum_ % k
            for pos in count[rem]:
                if index - pos >= 2:
                    print(index, pos)
                    return True

            count[rem].append(index)

        return False
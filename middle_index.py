class Solution:
    def findMiddleIndex(self, nums) -> int:
        prefix_sum = [sum(nums[:i + 1]) for i in range(len(nums))]
        print(prefix_sum)

        for i in range(len(nums)):
            if i == 0:
                if prefix_sum[-1] - prefix_sum[i] == 0:
                    return i
            elif i == len(nums) - 1:
                if prefix_sum[i - 1] == 0:
                    return i
            else:
                if prefix_sum[i - 1] == prefix_sum[-1] - prefix_sum[i]:
                    return i
        return -1
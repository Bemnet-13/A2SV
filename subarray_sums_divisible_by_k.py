class Solution:
    def subarraysDivByK(self, nums, k: int) -> int:
        count = 0
        prefix_sum = 0
        remainder_map = {0 : 1}

        for num in nums:
            prefix_sum += num
            mod = prefix_sum % k
            if mod < 0:
                mod += k
            if mod in remainder_map:
                count += remainder_map[mod]
                remainder_map[mod] += 1
            else:
                remainder_map[mod] = 1

        return count

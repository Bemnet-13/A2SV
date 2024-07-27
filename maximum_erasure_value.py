class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = r = score = max_score = 0
        seen = set()
        while l < len(nums) and r < len(nums):
            if nums[r] not in seen:
                seen.add(nums[r])
                score += nums[r]
                r += 1
            else:
                seen.remove(nums[l])
                score -= nums[l]
                l += 1
            max_score = max(max_score, score)

        return max_score
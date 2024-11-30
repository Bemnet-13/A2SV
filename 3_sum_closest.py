class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        print(nums)
        closest_sum = nums[-1] + nums[-2] + nums[-3]
        min_diff = abs(closest_sum - target)
        map_ = {min_diff : closest_sum}
        n = len(nums)

        for i in range(n):
            l, r = i + 1, n - 1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                # if min_diff > abs(curr_sum - target):
                distance = abs(curr_sum - target)
                min_diff = min(distance, min_diff)
                map_[distance] = curr_sum
                if curr_sum > target:
                    r -= 1
                elif curr_sum < target:
                    l += 1
                else:
                    break

        return map_[min_diff]
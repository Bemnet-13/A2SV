from collections import Counter
class Solution:
    def threeSum(self, nums):
        nums.sort()
        print(nums)
        solution = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target =  - 1 * nums[i]
            l = 0
            r = len(nums) - 1
            while l < r:
                if l == i:
                    l += 1
                    continue
                elif r == i:
                    r -= 1
                    continue
                if nums[l] + nums[r] == target:
                    n = Counter([nums[l], nums[r], nums[i]])
                    if n not in solution:
                        solution.append(n)
                    l += 1
                    
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1

        res = []
        for item in solution:
            ans = []
            for k in item:
                f = item[k]
                for _ in range(f):
                    ans.append(k)
            res.append(ans)

        return res
    
trial = Solution()
o = trial.threeSum([-1,-12,14,-6,4,-11,2,-7,13,-15,-1,11,-15,-15,13,-9,-11,-10,-7,-13,7,9,-13,-3,10,1,-5,12,11,-9,2,-4,-6,-7,5,5,-2,14,13,-12,14,-3,14,14,-11,5,12,-6,10,-9,-4,-6,-15,-9,-1,2,-1,9,-9,-5,-15,8,-2,-6,9,10,7,14,9,5,-13,9,-12,8,8,-8,-2,-2,1,-15,-4,5,-13,-4,3,1,5,-13,-13,11,-11,10,5,3,11,-9,-2,3,-10,-7,-6,14,9,-11,7,2,-4,13,7,5,13,-12,-13,7,-9,5,-7,11,-1,-12,8,3,13,-10,13,1,-4])
print(o)
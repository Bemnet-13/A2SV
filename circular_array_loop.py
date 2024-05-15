class Solution:
    def circularArrayLoop(self, nums) -> bool:
        l = 0
        size = len(nums)
        nums = 2 * nums 

        while l < size:
            p = l
            count = 0
            while True:
                i = nums[p]
                r = p + nums[p]
                if r < 0:
                    r += size

                if i * (nums[r % size]) < 0:
                    l += 1
                    break
                else:
                    count += 1
                    if r == l + size and count > 1:
                        return True
                    elif r == l + size and count == 1:
                        l += 1
                        break
                    elif r > l + size:
                        l += 1
                        break
                    else:
                        p = r
        return False
    
trial = Solution()
o = trial.circularArrayLoop(nums = [1,2,3,4,5])
print(o)                    

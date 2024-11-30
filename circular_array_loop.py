class Solution:
    def circularArrayLoop(self, nums) -> bool:
        n = len(nums)
        for i in range(n):
            starting = i
            curr = starting
            k = 0
            seen = set([starting]) 
            while k < n:
                next_ = (curr + nums[curr]) % n
                if not self.sameSign(nums[starting], nums[next_]):
                    break
                k += 1
                curr = next_
                seen.add(curr)
                if k > 1 and starting == curr and len(seen) >= 2:
                    return True
        return False
    
    def sameSign(self, a, b):
        if (a > 0 and b > 0) or (a < 0 and b < 0):
            return True
        return False

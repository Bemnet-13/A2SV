class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        
        l = 1
        r = x

        while l < r:
            mid = (l + r) // 2
            # print("l", l)
            # print("mid", mid)
            # print("r", r)
            res = mid * mid
            if res == x or l == mid:
                return mid
            elif res > x:
                r = mid 
            else:
                l = mid
        return l
    
trial = Solution()
o = trial.mySqrt(8)
print(o)